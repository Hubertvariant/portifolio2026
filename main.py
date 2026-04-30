


import streamlit as st

def carregar_codigo(nome_arquivo):
    try:
        # Tenta ler o arquivo localmente
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"// Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"// Erro inesperado: {e}"

st.set_page_config(
    page_title="Portfólio do Hubert",
    page_icon="👋",
    layout="wide"
)

# --- DEFINIÇÃO DOS TEMAS ---
TEMAS = {
    "JavaScript": {
        "bg": "linear-gradient(135deg, #ffee00 0%, #ffcc00 100%)",
        "header": "linear-gradient(to right, #1a1a1a 0%, #333 100%)",
        "text_header": "#ffee00",
        "content_bg": "#ffffff",
        "content_text": "#1a1a1a",
        "lang": "javascript",
        "card_text": "#000000",
        "card_bg": "rgba(0, 0, 0, 0.05)"
    },
    "Python": {
        "bg": "linear-gradient(135deg, #0f87cc 0%, #203a43 100%)",
        "header": "linear-gradient(to right, #ff9100 0%, #ff6a00 100%)",
        "text_header": "#ffffff",
        "content_bg": "#1e1e26",
        "content_text": "#e0e0e0",
        "lang": "python",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.1)"
    },
    "Analise": {
        "bg": "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)",
        "header": "linear-gradient(to right, #ffffff 0%, #e0e0e0 100%)",
        "text_header": "#0f0c29",
        "content_bg": "rgba(255, 255, 255, 0.05)",
        "content_text": "#ffffff",
        "lang": "markdown",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.1)"
    },
    "Mobile": {
        "bg": "linear-gradient(135deg, #6a11cb 0%, #2575fc 100%)",
        "header": "linear-gradient(to right, #00d2ff 0%, #3a7bd5 100%)",
        "text_header": "#ffffff",
        "content_bg": "#f8f9fa",  # Cor de fundo clara para destacar o QR Code
        "content_text": "#1e293b", # Texto escuro para contraste
        "lang": "markdown",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.15)"
    }
}

# --- SIDEBAR ---
opcao = st.sidebar.radio("Menu de Projetos", list(TEMAS.keys()))

# --- CSS DINÂMICO ---
t = TEMAS[opcao]
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ 
        background: {t['bg']}; 
        color: {t['content_text']};
    }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    .custom-card {{
        background-color: {t['card_bg']};
        color: {t['card_text']};
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }}
    div[data-testid="stExpander"] {{
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border-radius: 12px !important;
        margin-bottom: 1rem;
    }}
    div[data-testid="stExpander"] details summary {{
        background: {t['header']};
        color: {t['text_header']};
        padding: 15px 20px;
        font-weight: bold;
    }}
    div[data-testid="stExpander"] details div[data-testid="stExpanderDetails"] {{
        background-color: {t['content_bg']} !important;
        color: {t['content_text']} !important;
    }}
    a {{ color: {t['card_text']} !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS ---
projetos = []
exercicios = []

if opcao == "JavaScript":
    titulo = "JavaScript"
    projetos = [
        {"nome": "Teste em html", "arquivo": "JS/teste.html"},
        {"nome": "Carros JS", "arquivo": "JS/carros.js"},
        {"nome": "Lista de Livros", "arquivo": "JS/listaLivros.js"}
        # ... adicione os outros conforme necessário
    ]

elif opcao == "Python":
    titulo = "Python"
    projetos = [
        {"nome": "Automação Alura", "arquivo": "PY/automacaoAlura.py"},
        {"nome": "Dobro, Triplo, Raiz", "arquivo": "PY/DobroTriploRaizquadrada.py"}
    ]
    for i in range(1, 89):
        num = f"{i:03}"
        exercicios.append({"nome": f"Exercício {i}", "arquivo": f"CursoemV-PYTHON/ex{num}.py"})

elif opcao == "Analise":
    titulo = "📑 Análise"
    projetos = [
        {"nome": "Propriedade Intelectual", "link": "https://gamma.app/..."},
        {"nome": "Panorama Global 2026", "link": "https://gamma.app/..."}
    ]

elif opcao == "Mobile":
    titulo = "📱 Desenvolvimento Mobile"
    projetos = [
        {"nome": "Carrossel de Imagens", "imagem": "QRcode/QRcode_CarroselDeImagem.png"},
        {"nome": "Quem Faz?", "link": "https://github.com/Hubertvariant/quem-faz-app"},
        {"nome": "ItataU", "link": "https://github.com/Hubertvariant/ItataU"},
        {"nome": "Salva Mecânico", "link": "https://github.com/Hubertvariant/salva-mecanico"},
    ]

# --- RENDERIZAÇÃO ---
if projetos:
    projNumero = len(projetos)
    projUltimo = projetos[-1]

    st.title(titulo)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="custom-card"><h4>📁 {projNumero} Projetos</h4><p>Total nesta seção</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="custom-card"><h4>🚀 Último Projeto</h4><p>{projUltimo["nome"]}</p></div>', unsafe_allow_html=True)

    st.write("---")

    for projeto in projetos:
        with st.expander(projeto["nome"]):
            if "arquivo" in projeto:
                st.markdown(f"**📄 Arquivo:** `{projeto['arquivo']}`")
                conteudo = carregar_codigo(projeto["arquivo"])
                lang = "html" if projeto["arquivo"].endswith(".html") else t.get("lang", "python")
                st.code(conteudo, language=lang)
            
            elif "link" in projeto:
                st.markdown(f'<a href="{projeto["link"]}" target="_blank">Abrir documento completo →</a>', unsafe_allow_html=True)
            
            elif "imagem" in projeto:
                # Título centralizado com cor adaptada
                st.markdown(f"<h3 style='text-align: center; color: {t['content_text']};'>🔗 Escaneie para Testar</h3>", unsafe_allow_html=True)
                
                col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
                with col_img2:
                    # Adicionamos um fundo branco direto na imagem se necessário, 
                    # mas com o content_bg claro acima, já deve funcionar perfeitamente.
                    st.image(projeto["imagem"], caption=f"QR Code: {projeto['nome']}", use_container_width=True)

# --- SEÇÃO DE EXERCÍCIOS (EXCLUSIVO PYTHON) ---
if opcao == "Python" and exercicios:
    st.write("---")
    st.markdown("### 📝 Exercícios de Lógica")
    for ex in exercicios:
        with st.expander(ex["nome"]):
            cod = carregar_codigo(ex["arquivo"])
            st.code(cod, language="python")
