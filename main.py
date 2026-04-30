import streamlit as st

def carregar_codigo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"// Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"// Erro inesperado: {e}"

st.set_page_config(page_title="Portfólio do Hubert", page_icon="👨‍💻", layout="wide")

# --- DICIONÁRIO DE TEMAS PERSONALIZADOS ---
TEMAS = {
    "JavaScript": {
        "bg": "#F7DF1E", # Amarelo JS
        "card": "#000000",
        "text": "#000000",
        "btn_header": "#323330",
        "btn_text": "#F7DF1E",
        "icon": "🟨"
    },
    "Python": {
        "bg": "#3776AB", # Azul Python
        "card": "#FFE873", # Amarelo Python
        "text": "#ffffff",
        "btn_header": "#FFD43B",
        "btn_text": "#3776AB",
        "icon": "🐍"
    },
    "Games": {
        "bg": "#2D033B", # Roxo Neon
        "card": "#810CA8",
        "text": "#00FFA3", # Verde Matrix
        "btn_header": "#C147E9",
        "btn_text": "#ffffff",
        "icon": "🎮"
    },
    "Analise": {
        "bg": "#F0F2F6", # Cinza Claro Profissional
        "card": "#ffffff",
        "text": "#1F1F1F",
        "btn_header": "#007BFF",
        "btn_text": "#ffffff",
        "icon": "📊"
    },
    "Mobile": {
        "bg": "linear-gradient(135deg, #6a11cb 0%, #2575fc 100%)",
        "card": "rgba(255, 255, 255, 0.2)",
        "text": "#ffffff",
        "btn_header": "#ffffff",
        "btn_text": "#2575fc",
        "icon": "📱"
    }
}

# Interface
opcao = st.sidebar.radio("Escolha a Seção", list(TEMAS.keys()))
t = TEMAS[opcao]

# --- CSS DINÂMICO ---
st.markdown(f"""
    <style>
    /* Fundo da App */
    .stApp {{
        background: {t['bg']};
        color: {t['text']};
    }}
    
    /* Custom Card */
    .custom-card {{
        background-color: {t['card']};
        padding: 20px;
        border-radius: 15px;
        color: {t['text'] if opcao != 'Python' else '#3776AB'};
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        text-align: center;
    }}

    /* Estilo dos Expanders */
    .stExpander {{
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        border: 1px solid {t['btn_header']} !important;
    }}
    
    /* Títulos e Textos */
    h1, h2, h3, p {{
        color: {t['text']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS ---
if opcao == "Games":
    titulo = f"{t['icon']} HUB DE GAMES"
    projetos = [
        {"nome": "Super Mario Clone", "arquivo": "GAMES/mario.py"},
        {"nome": "Space Invaders", "arquivo": "GAMES/space.py"}
    ]
elif opcao == "JavaScript":
    titulo = f"{t['icon']} JAVASCRIPT"
    projetos = [{"nome": "Sistema de Login", "arquivo": "JS/login.js"}]
else:
    # Mantém a lógica que já tinhas para as outras seções...
    titulo = f"{t['icon']} {opcao}"
    projetos = [] 

# --- RENDERIZAÇÃO ---
st.title(titulo)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="custom-card">🚀 {len(projetos)} Projetos Disponíveis</div>', unsafe_allow_html=True)

st.write("---")

for p in projetos:
    with st.expander(p["nome"]):
        if "arquivo" in p:
            st.info(f"Caminho: {p['arquivo']}")
            codigo = carregar_codigo(p["arquivo"])
            st.code(codigo, language="python" if opcao != "JavaScript" else "javascript")
