import streamlit as st

def carregar_codigo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"// Erro: O arquivo '{nome_arquivo}' não foi encontrado localmente."
    except Exception as e:
        return f"// Erro inesperado: {e}"

st.set_page_config(
    page_title="Portfólio do Hubert",
    page_icon="👨‍💻",
    layout="wide"
)

# --- CONFIGURAÇÃO DE TEMAS ---
TEMAS = {
    "JavaScript": {
        "bg": "linear-gradient(135deg, #f7df1e 0%, #d4bb00 100%)",
        "header": "#1a1a1a", "text_header": "#f7df1e", "card_bg": "rgba(0,0,0,0.05)",
        "content_bg": "#ffffff", "content_text": "#1a1a1a", "lang": "javascript"
    },
    "Python": {
        "bg": "linear-gradient(135deg, #3776ab 0%, #2b5b84 100%)",
        "header": "#ff9100", "text_header": "#ffffff", "card_bg": "rgba(255,255,255,0.1)",
        "content_bg": "#1e1e26", "content_text": "#e0e0e0", "lang": "python"
    },
    "Games": {
        "bg": "linear-gradient(135deg, #000000 0%, #434343 100%)",
        "header": "linear-gradient(to right, #ff004c, #7000ff)",
        "text_header": "#ffffff", "card_bg": "rgba(255,255,255,0.15)",
        "content_bg": "#121212", "content_text": "#00ff41", "lang": "python" # Estilo Matrix/Terminal
    },
    "Analise": {
        "bg": "linear-gradient(135deg, #0f0c29 0%, #302b63 100%)",
        "header": "#ffffff", "text_header": "#0f0c29", "card_bg": "rgba(255,255,255,0.1)",
        "content_bg": "rgba(255,255,255,0.05)", "content_text": "#ffffff", "lang": "markdown"
    },
    "Mobile": {
        "bg": "linear-gradient(135deg, #6a11cb 0%, #2575fc 100%)",
        "header": "#00d2ff", "text_header": "#ffffff", "card_bg": "rgba(255,255,255,0.15)",
        "content_bg": "#f8f9fa", "content_text": "#1e293b", "lang": "markdown"
    }
}

opcao = st.sidebar.selectbox("Navegar por Categoria", list(TEMAS.keys()))
t = TEMAS[opcao]

# --- CSS CUSTOMIZADO ---
st.markdown(f"""
    <style>
    .main {{ background: {t['bg']}; color: {t['content_text']}; }}
    .stExpander {{ border: 1px solid rgba(255,255,255,0.2) !important; border-radius: 10px !important; }}
    .custom-card {{
        background: {t['card_bg']};
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(5px);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE CONTEÚDO ---
projetos = []
exercicios = []

if opcao == "Games":
    titulo = "🎮 Meus Jogos"
    projetos = [
        {"nome": "Snake Game", "arquivo": "GAMES/snake.py", "obs": "Requer Pygame instalado."},
        {"nome": "Pong", "arquivo": "GAMES/pong.py", "obs": "Rodar com Python 3.10+"}
    ]
elif opcao == "JavaScript":
    titulo = "黄 JavaScript"
    projetos = [{"nome": "Teste em html", "arquivo": "JS/teste.html"}]
elif opcao == "Python":
    titulo = "🐍 Python"
    projetos = [{"nome": "Automação", "arquivo": "PY/automacao.py"}]
    # Gerador de exercícios simplificado
    exercicios = [{"nome": f"Exercício {i}", "arquivo": f"CursoemV-PYTHON/ex{i:03}.py"} for i in range(1, 10)]
elif opcao == "Analise":
    titulo = "📊 Análise de Dados"
    projetos = [{"nome": "Relatório Gamma", "link": "https://gamma.app"}]
elif opcao == "Mobile":
    titulo = "📱 Mobile"
    projetos = [{"nome": "App Vendas", "imagem": "QRcode/vendas.png"}]

# --- RENDERIZAÇÃO ---
st.title(titulo)

# Resumo em colunas
c1, c2 = st.columns(2)
with c1: st.markdown(f'<div class="custom-card"><h3>{len(projetos)}</h3><p>Projetos</p></div>', unsafe_allow_html=True)
with c2: st.markdown(f'<div class="custom-card"><h3>Recente</h3><p>{projetos[0]["nome"] if projetos else "---"}</p></div>', unsafe_allow_html=True)

st.divider()

for p in projetos:
    with st.expander(f"📂 {p['nome']}"):
        if "arquivo" in p:
            if "obs" in p: st.info(p["obs"])
            st.code(carregar_codigo(p["arquivo"]), language=t["lang"])
        elif "link" in p:
            st.link_button("Ver Projeto Online", p["link"])
        elif "imagem" in p:
            st.image(p["imagem"], width=300)

# Exercícios (Python)
if exercicios and opcao == "Python":
    st.subheader("📝 Desafios de Lógica")
    for ex in exercicios:
        with st.expander(ex["nome"]):
            st.code(carregar_codigo(ex["arquivo"]))
