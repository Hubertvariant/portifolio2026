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

# Definição dos temas e metadados
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
        "bg": "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)",
        "header": "linear-gradient(to right, #ffffff 0%, #e0e0e0 100%)",
        "text_header": "#0f0c29",
        "content_bg": "rgba(255, 255, 255, 0.05)",
        "content_text": "#ffffff",
        "lang": "markdown",
        "card_text": "#ffffff",
        "card_bg": "rgba(255, 255, 255, 0.1)"
    }
}

# --- SIDEBAR ---
opcao = st.sidebar.radio("Menu de Projetos", list(TEMAS.keys()))

# --- APLICAÇÃO DO CSS DINÂMICO ---
t = TEMAS[opcao]
st.markdown(f"""
    <style>
    /* Fundo Principal */
    [data-testid="stAppViewContainer"] {{ 
        background: {t['bg']}; 
        color: {t['content_text']};
    }}
    
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}

    /* Cartões Personalizados de Informação */
    .custom-card {{
        background-color: {t['card_bg']};
        color: {t['card_text']};
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }}
    
    .custom-card h4 {{
        margin: 0;
        color: {t['card_text']};
    }}

    /* Estilização dos Expanders (Projetos) */
    div[data-testid="stExpander"] {{
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border-radius: 12px !important;
        margin-bottom: 1rem;
        background-color: transparent !important;
    }}

    div[data-testid="stExpander"] details {{
        border-radius: 12px !important;
        overflow: hidden;
        border: none !important;
    }}

    div[data-testid="stExpander"] details summary {{
        background: {t['header']};
        color: {t['text_header']};
        padding: 15px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }}

    div[data-testid="stExpander"] details summary:hover {{
        filter: brightness(1.2);
        transform: translateY(-2px);
    }}

    /* Conteúdo Interno do Expander */
    div[data-testid="stExpander"] details div[data-testid="stExpanderDetails"] {{
        background-color: {t['content_bg']} !important;
        color: {t['content_text']} !important;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.1);
    }}

    div[data-testid="stExpander"] details summary svg {{ 
        fill: {t['text_header']}; 
    }}
    
    /* Estilo para links globais */
    a {{
        color: {t['card_text']} !important;
        text-decoration: none;
        font-weight: bold;
    }}
    a:hover {{
        text-decoration: underline;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DADOS ---
if opcao == "JavaScript":
    titulo = "JavaScript"
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
            {"nome": "Usando Break", "arquivo": "JS/usandoBreak.js"},
            {"nome": "Break e Continue", "arquivo": "JS/breake_continue.js"},
            {"nome": "Objeto", "arquivo": "JS/objeto.js"},
            {"nome": "Filtro de Objetos", "arquivo": "JS/filtrar.js"},
            {"nome": "Colchetes com JS", "arquivo": "JS/colchete.js"},
            {"nome": "Substring com JS", "arquivo": "JS/substring.js"},
            {"nome": "Objetos 2 com JS", "arquivo": "JS/objet2.js"},
            {"nome": "Alterar Objetos", "arquivo": "JS/alterar.js"},
            {"nome": "Leitura de arquivos", "arquivo": "JS/2.leitura.js"},
            {"nome": "Cliente", "arquivo": "JS/2.cliente.json"},
            {"nome": "Conjunto de Números", "arquivo": "JS/conjuntoNumeros.js"},
            {"nome": "Lista de Livros", "arquivo": "JS/listaLivros.js"},
            {"nome": "Organizando Arrays", "arquivo": "JS/OrganizandoLista.js"}
        ]

elif opcao == "Python":
    titulo = "Python"
    projetos = [
            {"nome": "Dobro, Triplo, Raiz", "arquivo": "PY/DobroTriploRaizquadrada.py"},
            {"nome": "Média aritimética", "arquivo": "PY/MediaAritmetica.py"},
            {"nome": "Conversão Dolar", "arquivo": "PY/ConversãoDeReaisParaDolar.py"},
            {"nome": "Tinta para Parede", "arquivo": "PY/TintaParaParede.py"},
            {"nome": "Conversão Temperaturas", "arquivo": "PY/ConversãoDeTemperaturas.py"},
            {"nome": "Parte inteira de um número", "arquivo": "PY/ParteInteiraDeUmNumeroFloat.py"},
            {"nome": "Ordem de apresentação", "arquivo": "PY/ordemDeApresentação.py"},
            {"nome": "Lendo números", "arquivo": "PY/lendoNumeros.py"},
            {"nome": "Aluno para apagar o quadro", "arquivo": "PY/alunoSorteadoParaApagarOQuadro.py"},
            {"nome": "Hipotenusa de um Triangulo", "arquivo": "PY/hipotenusa.py"},
            {"nome": "Dividindo Nome", "arquivo": "PY/DividindoNome.py"},
            {"nome": "Colocando em maiúsculas", "arquivo": "PY/colocandoEmMaiuscolas.py"},
            {"nome": "Automação Alura", "arquivo": "PY/automacaoAlura.py"}
        ]

    exercicios = []

    for i in range(1, 89):
        num_formatado = f"{i:03}"
        
        exercicio = {
            "nome": f"Exercício {i}",
            "arquivo": f"CursoemV-PYTHON/ex{num_formatado}.py"
        }
        exercicios.append(exercicio)

elif opcao == "Analise":
    titulo = "📑 Análise"
    projetos = [
        {"nome": "Propriedade Intelectual e seus Direitos", "link": "https://gamma.app/docs/A-Importancia-da-Propriedade-Intelectual-e-Seus-Direitos-qjd90lyps67wxim?mode=doc"},
        {"nome": "Gestão Escolar: App Meu Horário", "link": "https://gamma.app/docs/Transforme-a-Gestao-Escolar-com-o-Meu-Horario-6n5bxnksgr5x4te"},
        {"nome": "Plano de Negócios: Meu Horário", "link": "https://gamma.app/docs/AGENDA-ESCOLAR-O-Fim-do-Papel-e-o-Inicio-da-Eficiencia-Inteligent-fptrgjoq0w5ikxc"},
        {"nome": "Panorama Global de Startups 2026", "link": "https://gamma.app/docs/Panorama-Global-de-Startups-2026-4xg3oj9glclqp0v?mode=doc"},
        {"nome": "Métricas e Melhorias Contínuas nos Negócios", "link": "https://gamma.app/docs/Metricas-e-Melhorias-Continuas-nos-Negocios-r4n7h2cqwz74hxg"}
    ]
elif opcao == "Mobile":
    titulo = "Mobile"
    projetos = [
        {"nome": "Carrossel de Imagens", "imagem": "data:image/png;base64,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"},
    ]


# --- RENDERIZAÇÃO ---
projNumero = len(projetos)
projUltimo = projetos[-1]

st.title(titulo)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <div class="custom-card">
                <h4>📁 {projNumero} Projetos</h4>
                <p style="margin:0; opacity: 0.8;">Total nesta seção</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="custom-card">
                <h4>🚀 Último Projeto</h4>
                <p style="margin:0; opacity: 0.8;">{projUltimo['nome']}</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")

    for projeto in projetos:
        with st.expander(projeto["nome"]):
            if "arquivo" in projeto:
                st.markdown(f"**📄 Local do Arquivo:** `{projeto['arquivo']}`")
                conteudo = carregar_codigo(projeto["arquivo"])
                extensao = projeto["arquivo"].split(".")[-1]
                lang = "html" if extensao == "html" else t.get("lang", "txt")
                st.code(conteudo, language=lang)
            
            elif "link" in projeto:
                st.markdown("### 🔗 Documentação Externa")
                st.write("Este projeto contém análises detalhadas e planejamento estratégico.")
                st.markdown(f'<a href="{projeto["link"]}" target="_blank">Abrir documento completo →</a>', unsafe_allow_html=True)
            elif "image" in projeto:
                st.markdown("### 🔗 QRCode")
                st.write(f"QRCode do projeto {projeto["nome"]}")
                st.markdown(f'<img src="{projeto["imagem"]}"/>', unsafe_allow_html=True)

if opcao == "Python":
    exerNumero = len(exercicios)
    exerUltimo = exercicios[-1]
    with st.container():
        st.markdown("### 📝 Exercícios")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class="custom-card">
                    <h4>📁 {exerNumero} Exercícios realizados</h4>
                    <p style="margin:0; opacity: 0.8;">Total nesta seção</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="custom-card">
                    <h4>🚀 Último Exercício</h4>
                    <p style="margin:0; opacity: 0.8;">{exerUltimo['nome']}</p>
                </div>
            """, unsafe_allow_html=True)

            st.write("---")
        for exercicio in exercicios:
            with st.expander(exercicio["nome"]):
                st.markdown(f"**📄 Local do Arquivo:** `{exercicio['arquivo']}`")
                conteudo = carregar_codigo(exercicio["arquivo"])
                extensao = exercicio["arquivo"].split(".")[-1]
                lang = "html" if extensao == "html" else t.get("lang", "txt")
                st.code(conteudo, language=lang)
