import streamlit as st
import os

# --- FUNÇÕES DE APOIO ---

def carregar_codigo(caminho_arquivo):
    """Lê o conteúdo de arquivos de texto/código."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"// Erro ao carregar: {e}"

def listar_arquivos_inteligente(pasta):
    """Varre a pasta e classifica os arquivos por tipo."""
    dados = []
    if os.path.exists(pasta):
        for item in sorted(os.listdir(pasta)):
            caminho = os.path.join(pasta, item)
            if os.path.isfile(caminho):
                ext = item.lower().split('.')[-1]
                
                tipo = "texto"
                if ext in ['png', 'jpg', 'jpeg', 'webp', 'gif']:
                    tipo = "imagem"
                elif ext in ['py', 'js', 'html', 'css', 'sql']:
                    tipo = "codigo"
                
                dados.append({
                    "nome": item,
                    "caminho": caminho,
                    "tipo": tipo,
                    "ext": ext
                })
    return dados

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio do Hubert",
    page_icon="👨‍💻",
    layout="wide"
)

# --- TEMAS PERSONALIZADOS (UI/UX) ---
TEMAS = {
    "JavaScript": {
        "bg": "linear-gradient(135deg, #f7df1e 0%, #d4bb00 100%)",
        "header": "#1a1a1a", "text_h": "#f7df1e", "card": "rgba(0,0,0,0.1)",
        "content_bg": "#ffffff", "content_text": "#1a1a1a", "lang": "javascript",
        "pasta": "JS", "desc": "Scripts e Front-end"
    },
    "Python": {
        "bg": "linear-gradient(135deg, #3776ab 0%, #2b5b84 100%)",
        "header": "#ff9100", "text_h": "#ffffff", "card": "rgba(255,255,255,0.1)",
        "content_bg": "#1e1e26", "content_text": "#e0e0e0", "lang": "python",
        "pasta": "PY", "desc": "Automações e Lógica"
    },
    "Games": {
        "bg": "linear-gradient(135deg, #000000 0%, #2d033b 100%)",
        "header": "linear-gradient(to right, #00ffa3, #03dac6)", "text_h": "#000000", 
        "card": "rgba(0, 255, 163, 0.1)", "content_bg": "#0a0a0a", "content_text": "#00ffa3", 
        "lang": "python", "pasta": "GAMES", "desc": "Desenvolvimento de Jogos"
    },
    "Mobile": {
        "bg": "linear-gradient(135deg, #6a11cb 0%, #2575fc 100%)",
        "header": "#ffffff", "text_h": "#2575fc", "card": "rgba(255,255,255,0.2)",
        "content_bg": "#f8f9fa", "content_text": "#1e293b", "lang": "markdown",
        "pasta": "QRcode", "desc": "Apps e QR Codes"
    },
    "Analise": {
        "bg": "linear-gradient(135deg, #0f0c29 0%, #302b63 100%)",
        "header": "#ffffff", "text_h": "#0f0c29", "card": "rgba(255,255,255,0.1)",
        "content_bg": "rgba(255,255,255,0.05)", "content_text": "#ffffff", "lang": "markdown",
        "pasta": "AP", "desc": "Insights e Dados"
    }
}

# --- SELEÇÃO DE TEMA ---
opcao = st.sidebar.radio("Navegar Projetos", list(TEMAS.keys()))
t = TEMAS[opcao]

# --- CSS INJETADO ---
st.markdown(f"""
    <style>
    .stApp {{ background: {t['bg']}; color: {t['content_text']}; }}
    
    .custom-card {{
        background: {t['card']};
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        text-align: center;
        margin-bottom: 20px;
    }}

    div[data-testid="stExpander"] {{
        background-color: {t['card']} !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 15px !important;
    }}

    div[data-testid="stExpander"] details summary {{
        background: {t['header']} !important;
        color: {t['text_h']} !important;
        padding: 15px;
        border-radius: 12px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE PRINCIPAL ---
st.title(f"Portfólio: {opcao}")
st.write(f"_{t['desc']}_")

# Busca automática dos arquivos na pasta
arquivos = listar_arquivos_inteligente(t["pasta"])

# Dashboard de Resumo
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="custom-card"><h2>{len(arquivos)}</h2><p>Ficheiros Detectados</p></div>', unsafe_allow_html=True)
with col2:
    status = "Online" if arquivos else "Vazio"
    st.markdown(f'<div class="custom-card"><h2>{status}</h2><p>Status da Pasta: /{t["pasta"]}</p></div>', unsafe_allow_html=True)

st.divider()

if not arquivos:
    st.warning(f"⚠️ Ninguém em casa! Adicione arquivos na pasta `{t['pasta']}`.")
else:
    for item in arquivos:
        with st.expander(f"📁 {item['nome'].upper()}"):
            
            # --- LÓGICA INTELIGENTE DE EXIBIÇÃO ---
            
            # 1. IMAGENS
            if item['tipo'] == "imagem":
                st.image(item['caminho'], use_container_width=True)
            
            # 2. CÓDIGOS
            elif item['tipo'] == "codigo":
                conteudo = carregar_codigo(item['caminho'])
                lang = "html" if item['ext'] == "html" else t['lang']
                st.code(conteudo, language=lang)
            
            # 3. TEXTO OU LINKS (.txt)
            else:
                conteudo = carregar_codigo(item['caminho']).strip()
                if conteudo.startswith("http"):
                    st.success("🔗 Link Externo Encontrado")
                    st.link_button(f"Aceder a {item['nome']}", conteudo)
                else:
                    st.info("Nota Informativa:")
                    st.write(conteudo)

# --- RODAPÉ ---
st.sidebar.divider()
st.sidebar.caption(f"Hubert © 2026 | Modo: {opcao}")
