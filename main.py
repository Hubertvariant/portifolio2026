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
    page_title="Portfólio Premium | Hubert",
    page_icon="👨‍💻",
    layout="wide"
)

# --- TEMAS PERSONALIZADOS (MODERNIZADOS) ---
TEMAS = {
    "JavaScript": {
        "bg": "linear-gradient(135deg, #111111 0%, #323330 100%)",
        "header": "#f7df1e", "text_h": "#000000", "card": "rgba(247, 223, 30, 0.1)",
        "content_bg": "#ffffff", "content_text": "#f7df1e", "lang": "javascript",
        "pasta": "JS", "desc": "✨ Interatividade e Front-end moderno"
    },
    "Python": {
        "bg": "linear-gradient(135deg, #021d33 0%, #033a63 100%)",
        "header": "linear-gradient(to right, #3776ab, #ffde57)", "text_h": "#021d33", 
        "card": "rgba(255, 255, 255, 0.05)", "content_bg": "#1e1e26", "content_text": "#ffffff", 
        "lang": "python", "pasta": "PY", "desc": "🐍 Automação e Inteligência de Dados"
    },
    "Games": {
        "bg": "linear-gradient(135deg, #0f0524 0%, #3b0a66 100%)",
        "header": "linear-gradient(to right, #00ffcc, #0088ff)", "text_h": "#000000", 
        "card": "rgba(0, 255, 204, 0.1)", "content_bg": "#0a0a0a", "content_text": "#00ffcc", 
        "lang": "python", "pasta": "GAMES", "desc": "🎮 Experiências Imersivas e Jogos"
    },
    "Mobile": {
        "bg": "linear-gradient(135deg, #0d0221 0%, #240b36 100%)",
        "header": "#e91e63", "text_h": "#ffffff", "card": "rgba(233, 30, 99, 0.1)",
        "content_bg": "#ffffff", "content_text": "#ffffff", "lang": "markdown",
        "pasta": "QRcode", "desc": "📱 Soluções Mobile e QR Codes"
    },
    "Analise": {
        "bg": "linear-gradient(135deg, #000428 0%, #004e92 100%)",
        "header": "#ffffff", "text_h": "#000428", "card": "rgba(255, 255, 255, 0.1)",
        "content_bg": "rgba(255, 255, 255, 0.05)", "content_text": "#ffffff", "lang": "markdown",
        "pasta": "AP", "desc": "📊 Transformando dados em decisões"
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
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(12px);
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}

    div[data-testid="stExpander"] {{
        background-color: rgba(0,0,0,0.2) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        margin-bottom: 10px;
    }}

    div[data-testid="stExpander"] details summary {{
        background: {t['header']} !important;
        color: {t['text_h']} !important;
        padding: 12px;
        border-radius: 10px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE PRINCIPAL ---
st.title(f"{opcao}")
st.markdown(f"#### {t['desc']}")

# Busca automática
arquivos = listar_arquivos_inteligente(t["pasta"])

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(f'<div class="custom-card"><h3 style="margin:0;">{len(arquivos)}</h3><p style="margin:0;">Projetos</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="custom-card"><h3 style="margin:0;">Ativo</h3><p style="margin:0;">Pasta: /{t["pasta"]}</p></div>', unsafe_allow_html=True)

st.write("") # Espaçador

if not arquivos:
    st.warning(f"ℹ️ Pasta `{t['pasta']}` vazia. Adicione arquivos para atualizar o portfólio.")
else:
    for item in arquivos:
        with st.expander(f"✨ {item['nome'].replace('_', ' ').upper()}"):
            
            # --- LÓGICA DE EXIBIÇÃO ---
            
            if item['tipo'] == "imagem":
                # Criamos 3 colunas e colocamos a imagem na do meio (menor)
                c_img1, c_img2, c_img3 = st.columns([1, 0.8, 1])
                with c_img2:
                    st.image(item['caminho'], caption=f"Visualização: {item['nome']}", use_container_width=True)
            
            elif item['tipo'] == "codigo":
                conteudo = carregar_codigo(item['caminho'])
                lang = "html" if item['ext'] == "html" else t['lang']
                st.code(conteudo, language=lang)
            
            else:
                conteudo = carregar_codigo(item['caminho']).strip()
                if conteudo.startswith("http"):
                    st.info(f"O projeto '{item['nome']}' está disponível externamente.")
                    st.link_button(f"🚀 ACESSAR PROJETO", conteudo, use_container_width=True)
                else:
                    st.markdown(f"> {conteudo}")

# --- SIDEBAR RODAPÉ ---
st.sidebar.divider()
st.sidebar.markdown(f"**Hubert Portfólio**")
st.sidebar.caption("© 2026 - Desenvolvido com Streamlit")
