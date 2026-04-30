import streamlit as st
import subprocess
import sys
import os
import tempfile
import time

def carregar_codigo(nome_arquivo):
    """Carrega o conteúdo de um arquivo"""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"// Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"// Erro inesperado: {e}"

def executar_pygame(arquivo):
    """Executa um arquivo Pygame em um processo separado"""
    try:
        # Verifica se o pygame está instalado
        subprocess.run([sys.executable, "-m", "pip", "show", "pygame"], 
                      capture_output=True, check=True)
        
        # Executa o arquivo em um processo separado
        processo = subprocess.Popen(
            [sys.executable, arquivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Aguarda um pouco para ver se inicia corretamente
        time.sleep(2)
        
        if processo.poll() is None:
            return f"✅ Jogo iniciado em janela separada! (PID: {processo.pid})"
        else:
            stderr = processo.stderr.read()
            return f"❌ Erro ao executar o jogo:\n```\n{stderr}\n```"
            
    except subprocess.CalledProcessError:
        return "❌ Pygame não está instalado. Execute: pip install pygame"
    except Exception as e:
        return f"❌ Erro inesperado: {e}"

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
        "content_bg": "#f8f9fa",
        "content_text": "#1e293b",
        "lang": "markdown",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.15)"
    },
    "Games": {  # Nova seção de Games
        "bg": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "header": "linear-gradient(to right, #f093fb 0%, #f5576c 100%)",
        "text_header": "#ffffff",
        "content_bg": "rgba(0, 0, 0, 0.7)",
        "content_text": "#ffffff",
        "lang": "python",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.15)",
        "game_bg": "#2d1b4e"
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
        transition: transform 0.3s ease;
    }}
    .custom-card:hover {{
        transform: translateY(-5px);
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
        border-radius: 12px 12px 0 0;
    }}
    div[data-testid="stExpander"] details div[data-testid="stExpanderDetails"] {{
        background-color: {t['content_bg']} !important;
        color: {t['content_text']} !important;
        padding: 20px;
    }}
    a {{ color: {t['card_text']} !important; font-weight: bold; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .game-button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        margin: 5px;
        transition: transform 0.2s;
    }}
    .game-button:hover {{
        transform: scale(1.05);
    }}
    .badge {{
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
        margin-left: 10px;
    }}
    .badge-pygame {{ background: #4CAF50; color: white; }}
    .badge-python {{ background: #2196F3; color: white; }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS ---
projetos = []
exercicios = []
games = []

if opcao == "JavaScript":
    titulo = "JavaScript"
    projetos = [
        {"nome": "Teste em html", "arquivo": "JS/teste.html"},
        {"nome": "Carros JS", "arquivo": "JS/carros.js"},
        {"nome": "Lista de Livros", "arquivo": "JS/listaLivros.js"},
        {"nome": "Calculadora", "arquivo": "JS/calculadora.js"},
        {"nome": "Jogo da Velha", "arquivo": "JS/jogoVelha.js"}
    ]

elif opcao == "Python":
    titulo = "Python"
    projetos = [
        {"nome": "Automação Alura", "arquivo": "PY/automacaoAlura.py"},
        {"nome": "Dobro, Triplo, Raiz", "arquivo": "PY/DobroTriploRaizquadrada.py"},
        {"nome": "Análise de Dados", "arquivo": "PY/analiseDados.py"},
        {"nome": "Web Scraping", "arquivo": "PY/webscraping.py"}
    ]
    for i in range(1, 89):
        num = f"{i:03}"
        exercicios.append({"nome": f"Exercício {i}", "arquivo": f"CursoemV-PYTHON/ex{num}.py"})

elif opcao == "Analise":
    titulo = "📑 Análise"
    projetos = [
        {"nome": "Propriedade Intelectual", "link": "https://gamma.app/..."},
        {"nome": "Panorama Global 2026", "link": "https://gamma.app/..."},
        {"nome": "Análise de Vendas", "link": "https://gamma.app/..."},
        {"nome": "Dashboard Financeiro", "link": "https://gamma.app/..."}
    ]

elif opcao == "Mobile":
    titulo = "📱 Desenvolvimento Mobile"
    projetos = [
        {"nome": "Carrossel de Imagens", "imagem": "QRcode/QRcode_CarroselDeImagem.png"},
        {"nome": "Quem Faz?", "link": "https://github.com/Hubertvariant/quem-faz-app"},
        {"nome": "ItataU", "link": "https://github.com/Hubertvariant/ItataU"},
        {"nome": "Salva Mecânico", "link": "https://github.com/Hubertvariant/salva-mecanico"},
        {"nome": "App de Tarefas", "link": "https://github.com/Hubertvariant/todo-app"}
    ]

elif opcao == "Games":
    titulo = "🎮 Games Portfolio"
    games = [
        {
            "nome": "Space Invaders",
            "descricao": "Clássico jogo de nave espacial com Pygame",
            "arquivo": "GAMES/space_invaders.py",
            "tipo": "pygame",
            "dificuldade": "Médio",
            "controles": "Setas para mover, Espaço para atirar"
        },
        {
            "nome": "Snake Game",
            "descricao": "Jogo da cobrinha moderno com pontuação",
            "arquivo": "GAMES/snake_game.py",
            "tipo": "pygame",
            "dificuldade": "Fácil",
            "controles": "Setas para direcionar a cobra"
        },
        {
            "nome": "Pong",
            "descricao": "Tênis de mesa multiplayer",
            "arquivo": "GAMES/pong.py",
            "tipo": "pygame",
            "dificuldade": "Médio",
            "controles": "W/S para Player 1, Setas para Player 2"
        },
        {
            "nome": "Jogo da Memória",
            "descricao": "Teste sua memória com cartas",
            "arquivo": "GAMES/memory_game.py",
            "tipo": "pygame",
            "dificuldade": "Fácil",
            "controles": "Clique nas cartas com o mouse"
        },
        {
            "nome": "Plataforma 2D",
            "descricao": "Jogo de plataforma simples",
            "arquivo": "GAMES/platformer.py",
            "tipo": "pygame",
            "dificuldade": "Difícil",
            "controles": "Setas para mover, Espaço para pular"
        },
        {
            "nome": "Quiz Game",
            "descricao": "Jogo de perguntas e respostas",
            "arquivo": "GAMES/quiz_game.py",
            "tipo": "terminal",
            "dificuldade": "Médio",
            "controles": "Digite o número da resposta"
        }
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
                st.markdown(f'<a href="{projeto["link"]}" target="_blank">🔗 Abrir documento completo →</a>', unsafe_allow_html=True)
            
            elif "imagem" in projeto:
                st.markdown(f"<h3 style='text-align: center; color: {t['content_text']};'>🔗 Escaneie para Testar</h3>", unsafe_allow_html=True)
                
                col_img1, col_img2, col_img3 = st.columns([1, 1, 1])
                with col_img2:
                    st.image(projeto["imagem"], caption=f"QR Code: {projeto['nome']}", use_container_width=True)

# --- SEÇÃO DE GAMES ---
if opcao == "Games" and games:
    # Estatísticas dos games
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="custom-card"><h4>🎮 {len(games)} Games</h4><p>Jogos disponíveis</p></div>', unsafe_allow_html=True)
    with col2:
        pygame_count = sum(1 for g in games if g.get('tipo') == 'pygame')
        st.markdown(f'<div class="custom-card"><h4>🎯 {pygame_count} Pygame</h4><p>Com interface gráfica</p></div>', unsafe_allow_html=True)
    with col3:
        terminal_count = sum(1 for g in games if g.get('tipo') == 'terminal')
        st.markdown(f'<div class="custom-card"><h4>💻 {terminal_count} Terminal</h4><p>Jogos no console</p></div>', unsafe_allow_html=True)

    st.write("---")
    
    # Informação sobre dependências
    with st.expander("📦 Dependências Necessárias", expanded=False):
        st.markdown("""
        Para jogar os jogos Pygame, você precisa instalar a biblioteca:
        ```bash
        pip install pygame
