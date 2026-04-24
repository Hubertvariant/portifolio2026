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
    titulo = "📑 Análise"
    projetos = [
        {"nome": "Propriedade Intelectual e seus Direitos", "link": "https://gamma.app/docs/A-Importancia-da-Propriedade-Intelectual-e-Seus-Direitos-qjd90lyps67wxim?mode=doc"},
        {"nome": "Gestão Escolar: App Meu Horário", "link": "https://gamma.app/docs/Transforme-a-Gestao-Escolar-com-o-Meu-Horario-6n5bxnksgr5x4te"},
        {"nome": "Plano de Negócios: Meu Horário", "link": "https://gamma.app/docs/AGENDA-ESCOLAR-O-Fim-do-Papel-e-o-Inicio-da-Eficiencia-Inteligent-fptrgjoq0w5ikxc"},
        {"nome": "Panorama Global de Startups 2026", "link": "https://gamma.app/docs/Panorama-Global-de-Startups-2026-4xg3oj9glclqp0v?mode=doc"},
        {"nome": "Métricas e Melhorias Contínuas nos Negócios", "link": "https://gamma.app/docs/Metricas-e-Melhorias-Continuas-nos-Negocios-r4n7h2cqwz74hxg"}
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
