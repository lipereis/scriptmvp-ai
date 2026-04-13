# scriptmvp-ai
Ferramenta de IA para gerar roteiros virais de Reels, TikTok e Shorts | Projeto de Portfólio de Prompt Engineering

markdown

# 🎬 ScriptMVP AI

**Do briefing ao roteiro viral em segundos**

Uma ferramenta de IA especializada em gerar roteiros profissionais e otimizados para conteúdo audiovisual curto (Reels, TikTok, YouTube Shorts, Stories e anúncios).

Desenvolvido como **primeiro projeto de portfólio de Prompt Engineering**.

---

## ✨ Funcionalidades

- Geração de roteiros completos em **Português, Inglês e Espanhol**
- Estrutura profissional com Hook forte, timing, texto na tela, B-roll, tom de voz e CTA
- Avaliação automática de **Viral Score**
- Interface simples e intuitiva feita com Streamlit
- Suporte ao modelo **Google Gemini 2.5 Flash**

---

## 🎯 Objetivo do Projeto

Este projeto foi criado para demonstrar minhas habilidades em **Prompt Engineering**, incluindo:

- Criação e iteração de System Prompts avançados
- Uso de técnicas como Chain-of-Thought, Few-shot examples e Output Structuring
- Controle de output com estrutura rígida
- Adaptação cultural e linguística (PT-BR, EN, ES)
- Refinamento contínuo baseado em testes

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit** (interface web)
- **Google Gemini API** (gemini-2.5-flash)
- **Prompt Engineering** (System Prompt + Few-shot)

---

## 🚀 Como rodar localmente

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/scriptmvp-ai.git
cd scriptmvp-ai

2. Crie e ative o ambiente virtualbash

python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

3. Instale as dependênciasbash

pip install -r requirements.txt

4. Rode a aplicaçãobash

streamlit run scriptmvp.py

5. Configure a API KeyAcesse Google AI Studio
Crie uma chave API
Cole na barra lateral da aplicação

 Estrutura do Projeto

scriptmvp-ai/
├── scriptmvp.py          # Arquivo principal da aplicação
├── requirements.txt      # Dependências
├── README.md
└── prompts/
    └── system_prompt_v2.md   # (opcional) Versões dos prompts

 Evolução do Prompt EngineeringDurante o desenvolvimento, refinei o System Prompt em 3 versões:v1.0: Prompt básico com estrutura
v2.0: Adição de Few-shot examples + regras mais rígidas
v3.0: Otimização para viralidade, retenção e linguagem natural (versão atual)

Principais técnicas aplicadas:Output structuring
Few-shot prompting
Role prompting
Constraint-based prompting
Multilingual adaptation

