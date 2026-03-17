import streamlit as st

def carregar_codigo(nome_arquivo):
    try:
        # Tenta ler o arquivo localmente
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"// Erro: O arquivo '{nome_arquivo}' não foi encontrado."

st.set_page_config(
    page_title="Portifólio do Hubert",
    page_icon="👋",
    layout="wide"
)

TEMAS = {
    "JavaScrpit": {
        "bg": "linear-gradient(to right, #ffee00d8 0%, #ffee00 100%)",
        "header": "linear-gradient(to right, #122500e8 0%, #122500 100%)",
        "text_header": "#7bff00",
        "content_bg": "#F0F2F6",
        "content_text": "#333",
        "lang": "javascript"
    },
    "Python": {
        "bg": "linear-gradient(to right, #0f87ccd8 0%, #0f87cc 100%)",
        "header": "linear-gradient(to right, #ff9100e8 0%, #ff9100 100%)",
        "text_header": "#fff",
        "content_bg": "#262730",
        "content_text": "#fff",
        "lang": "python"
    }
}

# --- SIDEBAR ---
opcao = st.sidebar.radio("Menu de Projetos", list(TEMAS.keys()))

# --- APLICAÇÃO DO CSS DINÂMICO ---
t = TEMAS[opcao]
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background: {t['bg']}; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}
    div[data-testid="stExpander"] details summary {{
        background: {t['header']};
        color: {t['text_header']};
        border-radius: 5px;
    }}
    div[data-testid="stExpander"] details div[data-testid="stExpanderDetails"] {{
        background-color: {t['content_bg']};
        color: {t['content_text']};
        padding: 15px;
        border-radius: 0 0 5px 5px;
    }}
    div[data-testid="stExpander"] details summary svg {{ fill: {t['text_header']}; }}
    </style>
    """, unsafe_allow_html=True)

if opcao == "JavaScrpit":


    titulo = "JavaScrpit"

    projetos = [
        {"nome": "Teste em html", "arquivo": "JS/teste.html"},
        {"nome": "Teste em JS", "arquivo": "JS/teste.js"},
        {"nome": "Teste 2 em JS", "arquivo": "JS/teste2.js"},
        {"nome": "Teste 3 em JS", "arquivo": "JS/teste3.js"},
        {"nome": "Carros JS", "arquivo": "JS/carros.js"},
        {"nome": "Notas com JS", "arquivo": "JS/notas.js"},
        {"nome": "Media com Condições", "arquivo": "JS/media_se.js"},
        {"nome": "Variaveis com JS", "arquivo": "JS/variaveis.js"},
        {"nome": "Operação basicas com JS", "arquivo": "JS/opercaobasica.js"},
        {"nome": "Arrays com JS", "arquivo": "JS/array.js"},
        {"nome": "Usando For", "arquivo": "JS/usandoFor.js"},
        {"nome": "Usando Break", "arquivo": "JS/usandoBreak.js"}
    ]
    
    projNumero = len(projetos)
    projUtimo = projetos[-1]

elif opcao == "Python":
    titulo = "Python"
    
    projetos = [
        {"nome": "Dobro, Triplo, Raiz", "arquivo": "PY/DobroTriploRaizquadrada.py"},
        {"nome": "Média aritimética", "arquivo": "PY/MediaAritmetica.py"},
        {"nome": "Conversão Dolar", "arquivo": "PY/ConversãoDeReaisParaDolar.py"},
        {"nome": "Tinta para Parede", "arquivo": "PY/TintaParaParede.py"},
        {"nome": "Conversão Temperaturas", "arquivo": "PY/ConversãoDeTemperaturas.py"}
    ]

    projNumero = len(projetos)
    projUtimo = projetos[-1]
elif opcao == "Analise":
    titulo = "Analise"
    #projNumero = len(projetos)


st.title(titulo)

with st.container():
    st.text(f"{projNumero} projetos")
    st.text(f"{projUtimo["nome"]}, Ultimo projeto")

    for projeto in projetos:
        with st.expander(projeto["nome"]):
            st.caption(f"Arquivo: `{projeto['arquivo']}`")
            if "link" in projeto:
                st.write(f"Link: {projeto['link']}")
            else:
                conteudo = carregar_codigo(projeto["arquivo"])
                extensao = projeto["arquivo"].split(".")[-1]
                lang = "html" if extensao == "html" else t["lang"]
                
                st.code(conteudo, language=lang)
