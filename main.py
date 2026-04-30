import streamlit as st
import os

# --- FUNÇÕES DE APOIO ---

def carregar_codigo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"// Erro ao ler arquivo: {e}"

def listar_conteudo_inteligente(diretorio):
    """ Varre a pasta e identifica o tipo de arquivo """
    itens_processados = []
    if os.path.exists(diretorio):
        for nome_arquivo in sorted(os.listdir(diretorio)):
            caminho_completo = os.path.join(diretorio, nome_arquivo)
            
            # Ignorar pastas, focar em arquivos
            if os.path.isfile(caminho_completo):
                extensao = nome_arquivo.lower().split('.')[-1]
                
                tipo = "texto"
                if extensao in ['png', 'jpg', 'jpeg', 'webp']:
                    tipo = "imagem"
                elif extensao in ['py', 'js', 'html', 'css']:
                    tipo = "codigo"
                
                itens_processados.append({
                    "nome": nome_arquivo,
                    "caminho": caminho_completo,
                    "tipo": tipo,
                    "extensao": extensao
                })
    return itens_processados

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="Portfólio Automático", layout="wide")

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

"content_bg": "#f8f9fa", # Cor de fundo clara para destacar o QR Code

"content_text": "#1e293b", # Texto escuro para contraste

"lang": "markdown",

"card_text": "#ffffff",

"card_bg": "rgba(255, 255, 255, 0.15)"

}

}

opcao = st.sidebar.radio("Menu", list(TEMAS.keys()))
t = TEMAS[opcao]

# --- LÓGICA DE RENDERIZAÇÃO ---
st.title(f"📂 Seção {opcao}")

# Busca os arquivos na pasta definida para o tema
arquivos = listar_conteudo_inteligente(t["pasta"])

if not arquivos:
    st.info(f"Adicione arquivos na pasta `{t['pasta']}` para visualizá-los aqui.")
else:
    for item in arquivos:
        with st.expander(f"📄 {item['nome']}"):
            
            # Inteligência de Exibição
            if item['tipo'] == "imagem":
                st.image(item['caminho'], caption=item['nome'], use_container_width=True)
                st.download_button("Baixar Imagem", item['caminho'], file_name=item['nome'])
                
            elif item['tipo'] == "codigo":
                conteudo = carregar_codigo(item['caminho'])
                # Se for HTML, o Streamlit destaca corretamente se passarmos a linguagem
                lang = "html" if item['extensao'] == "html" else t['lang']
                st.code(conteudo, language=lang)
                
            else:
                # Caso seja um arquivo de texto simples ou link
                conteudo = carregar_codigo(item['caminho'])
                if "http" in conteudo:
                    st.link_button(f"Abrir Link: {item['nome']}", conteudo.strip())
                else:
                    st.text(conteudo)

# --- CSS PARA CORES (Resumo) ---
st.markdown(f"<style>.stApp {{ background: {t['bg']}; }} </style>", unsafe_allow_html=True)
