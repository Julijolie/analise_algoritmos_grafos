# Sistema de Algoritmos de Grafos

## 📋 Informações do Projeto

- **Disciplina:** Análise e Complexidade de Algoritmos (IBM3121)
- **Professor:** Cassius Figueiredo
- **Curso:** Engenharia de Computação
- **Período:** 6°
- **Semestre:** 2025.1

---

## 👥 Integrante

- Juliana de Oliveira - [202203947729]

---

## 📖 Sobre o Sistema

Este sistema é uma aplicação web (Flask + HTML/JS/CSS) que demonstra a execução dos algoritmos **DFS** e **BFS**. A aplicação permite ao usuário selecionar um dos grafos pré-definidos, escolher um nó inicial e executar os algoritmos de busca. A estrutura do grafo é representada por **listas de adjacência** no backend e visualizada através de **imagens estáticas** no frontend. Os resultados, como ordem de visita, pais e distâncias, são apresentados em tabelas detalhadas.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x
- Navegador web

### Passos para Execução

1.  **Clone o Repositório:**

    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_GIT]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Instale as Dependências:**

    ```bash
    pip install Flask Flask-Cors
    ```

3.  **Execute o Backend:**

    ```bash
    python backend/app.py
    ```

    Mantenha este terminal aberto.

4.  **Abra o Frontend:**
    Navegue até a pasta `frontend` e abra o arquivo `index.html` no seu navegador.

---

## 🎯 Como Usar

1.  **Escolher Grafo:** Selecione um grafo no primeiro menu. A sua lista de adjacência e visualização gráfica aparecerão.
2.  **Escolher Nó Inicial:** Selecione o nó de partida.
3.  **Executar:** Clique em "Executar DFS" ou "Executar BFS".
4.  **Analisar:** Verifique a tabela de resultados na parte inferior da página.

---

## 🧪 Grafos de Teste

O sistema utiliza os dois grafos especificados no enunciado:

- **Grafo 1:** Não direcionado e com componentes desconexos.
- **Grafo 2:** Direcionado e conectado.

---

## 🔍 Detalhes dos Algoritmos

Ambos os algoritmos (DFS e BFS) foram implementados para lidar com grafos desconexos, garantindo que todos os nós sejam visitados.

- **Resultados do DFS:** Incluem ordem de visita, árvore de pais, tempos de descoberta (pré-ordem) e finalização (pós-ordem).
- **Resultados do BFS:** Incluem ordem de visita, árvore de pais e distâncias em relação ao nó inicial de cada componente.
