# Sistema de Algoritmos de Grafos

## 📋 Informações Gerais

- **Disciplina:** Análise e Complexidade de Algoritmos (IBM3121)
- **Professor:** Cassius Figueiredo
- **Curso:** Engenharia de Computação
- **Semestre:** 2025.1
- **Feito por:**
  - Juliana de Oliveira - [202203947729]

---

## 📖 Informações Relevantes sobre a Aplicação

Este projeto é uma aplicação web desenvolvida para a demonstração interativa dos algoritmos de busca **DFS (Depth-First Search)** e **BFS (Breadth-First Search)**.

A principal funcionalidade é um **editor gráfico visual** que permite ao utilizador criar o seu próprio grafo do zero, adicionando nós e arestas de forma intuitiva. O sistema permite ainda definir se o grafo criado é **direcionado ou não-direcionado**, ajustando a visualização e o comportamento das buscas de acordo.

A arquitetura é composta por:

- **Backend:** Uma API em **Python** com o micro-framework **Flask**, responsável por receber a estrutura do grafo criado pelo utilizador, convertê-la para uma **lista de adjacência**, executar os algoritmos e retornar os resultados.
- **Frontend:** Uma interface desenvolvida em **HTML, CSS e JavaScript**, que utiliza a biblioteca **Cytoscape.js** para renderizar o editor gráfico e apresenta os resultados dos algoritmos em tabelas formatadas.

---

## 🚀 Instruções Detalhadas de Execução

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Navegador web(Google Chrome, Firefox, etc.)

### Passos para Execução

1.  **Clonar o Repositório**
    Abra um terminal ou prompt de comando e clone o repositório do projeto para a sua máquina local:

    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_GIT]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Instalar as Dependências**
    Navegue até a pasta raiz do projeto no seu terminal e instale as bibliotecas Python necessárias com o seguinte comando:

    ```bash
    pip install Flask Flask-Cors
    ```

3.  **Executar o Servidor Backend**
    Ainda no terminal, execute o servidor Flask. Este comando iniciará a API que o frontend precisa para funcionar.

    ```bash
    python backend/app.py
    ```

    O terminal deverá exibir uma mensagem indicando que o servidor está rodando em `http://127.0.0.1:5000`. **É crucial que este terminal permaneça aberto** durante todo o uso da aplicação.

4.  **Abrir a Aplicação no Navegador**
    Com o servidor backend em execução, navegue até a pasta `frontend` no seu explorador de arquivos e abra o arquivo `index.html` com o seu navegador de preferência. A aplicação estará pronta para ser usada.
