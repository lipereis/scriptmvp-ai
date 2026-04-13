import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ScriptMVP AI", page_icon="🎬", layout="centered")

st.title("🎬 ScriptMVP AI")
st.markdown("**Do briefing ao roteiro viral em segundos** - Powered by Google Gemini")

#  CONFIGURAÇÃO 
with st.sidebar:
    st.header("🔑 Configuração")
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        help="Cole sua chave do Google AI Studio"
    )
    
    model_choice = st.selectbox(
        "Modelo Gemini",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite"],  # Flash é mais rápido e barato
        index=0
    )

#  SYSTEM PROMPT 
system_prompt = """Você é ScriptMVP AI, o melhor especialista mundial em roteiros para conteúdo audiovisual curto em 2026.

Sua missão é criar roteiros altamente viciantes, com excelente retenção e potencial viral para Reels, TikTok, YouTube Shorts e anúncios.

REGRAS OBRIGATÓRIAS:
- Responda SEMPRE no idioma solicitado (Português Brasileiro, English ou Español Latino).
- Linguagem 100% natural, humana e conversacional.
- Use gírias leves quando for PT-BR.
- Foque em apenas UMA ideia principal por vídeo.
- Hook muito forte nos primeiros 3 segundos.

ESTRUTURA OBRIGATÓRIA (siga exatamente nesta ordem):

1. **Título do Roteiro**
2. **Duração estimada**
3. **Hook** (primeiros 3-5 segundos)
4. **Roteiro completo** (dividido por tempo: 0-5s, 5-15s, etc.)
5. **Texto na tela (On-screen text)**
6. **Ideias de B-roll / Visuals**
7. **Tom de voz e sugestão de música**
8. **CTA Final**
9. **Viral Score (0-100)** + explicação curta
10. **2 Variações alternativas do Hook**

Agora gere o roteiro seguindo rigorosamente esta estrutura."""

# INTERFACE 
with st.form("script_form"):
    col1, col2 = st.columns(2)
    with col1:
        idioma = st.selectbox("🌐 Idioma", ["Português (PT-BR)", "English (EN)", "Español (ES)"])
    with col2:
        duracao = st.selectbox("⏱️ Duração", ["15 segundos", "30 segundos", "45 segundos", "60 segundos"])
    
    nicho = st.text_input("👥 Nicho e Público-alvo", placeholder="Ex: Mulheres 28-45 anos, clínica de estética em São Paulo")
    briefing = st.text_area("📝 Briefing / Ideia do vídeo", height=120, placeholder="Ex: Reel sobre botox com resultado natural...")
    
    submitted = st.form_submit_button("🚀 Gerar Roteiro", type="primary")

# GERAÇÃO 
if submitted:
    if not api_key:
        st.error("❌ Por favor, cole sua Gemini API Key na barra lateral.")
    elif not briefing or not nicho:
        st.error("❌ Preencha o nicho e o briefing.")
    else:
        with st.spinner("Gerando roteiro com Gemini... 🎥"):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_choice)
                
                full_prompt = f"{system_prompt}\n\nInput:\nIdioma: {idioma}\nDuração: {duracao}\nNicho e Público: {nicho}\nBriefing: {briefing}"
                
                response = model.generate_content(full_prompt)
                resultado = response.text
                
                st.success("✅ Roteiro gerado com sucesso!")
                st.markdown(resultado)
                
                st.download_button("📥 Baixar como TXT", data=resultado, file_name="roteiro_scriptmvp.txt")
                
            except Exception as e:
                st.error(f"Erro: {str(e)}")
                st.info("Verifique se a chave está correta e se você não ultrapassou o limite do free tier.")

st.caption("ScriptMVP AI • Portfólio de Prompt Engineering - Usando Google Gemini")