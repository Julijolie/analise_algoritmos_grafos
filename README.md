# Relatório Final: Sistema de Algoritmos de Grafos

## 1. Visão Geral do Projeto

Este documento apresenta os resultados e funcionalidades da aplicação web desenvolvida para a disciplina de **Análise e Complexidade de Algoritmos (IBM3121)**.  
O sistema, construído com um backend em **Python/Flask** e um frontend em **HTML/CSS/JavaScript**, cumpre todos os requisitos do enunciado, com foco principal na criação de grafos pelo utilizador e na correta execução e apresentação dos algoritmos de busca **DFS (Depth-First Search)** e **BFS (Breadth-First Search)**.

A principal funcionalidade é um **editor gráfico interativo**, que permite ao utilizador criar, visualizar e testar grafos personalizados de forma intuitiva.

---

## 2. Interface Principal da Aplicação

A interface foi desenhada para ser limpa e funcional, dividida em três áreas principais:

- **Editor de grafos**
- **Controlos de execução**
- **Área de resultados**

> ![Interface Principal da Aplicação](inserir-caminho-da-imagem-aqui)

### Editor de Grafo (Painel Esquerdo)

- **Como usar**: Instruções claras para o utilizador.
- **Ferramentas de Edição**: Botões para "Adicionar Nó" e "Criar Aresta".
- **Barra de Status**: Fornece feedback em tempo real durante a criação de arestas.
- **Opções do Grafo**: Permite definir se o grafo é direcionado, o que afeta tanto a visualização (com ou sem setas) como o cálculo da lista de adjacência no backend.

### Controlos de Execução

- Permite selecionar o nó inicial e executar os algoritmos diretamente do painel.

### Área de Visualização (Painel Direito)

- Renderiza o grafo em tempo real conforme o utilizador adiciona nós e arestas.

### Resultado do Algoritmo (Seção Inferior)

- Exibe os resultados completos da execução em tabelas bem formatadas.

---

## 3. Exemplo de Resultado Esperado: DFS em Grafo Desconexo

Para validar a implementação, criamos um **grafo não-direcionado e desconexo**, semelhante ao especificado no enunciado, mas com a estrutura que definimos (sem a ligação D-E).

### Cenário de Teste

- **Grafo**: Não-Direcionado, com o componente D-G-H separado.
- **Ação**: Executar DFS a partir do Nó V1.

> ![Resultado Esperado do DFS](inserir-caminho-da-imagem-do-dfs-aqui)

### Análise do Resultado

- **Ordem de Visita**: O algoritmo primeiro explora completamente o componente do nó inicial (V1, V2, V3...) e depois "salta" para o componente desconexo (V4, V7, V8) para garantir que todos os nós sejam visitados.

#### Tabela de Resultados

- **Pai**: Mostra corretamente a árvore de busca gerada. Note que V4 não tem pai, pois ele é o ponto de partida de um novo componente.
- **Pré-ordem e Pós-ordem**: A contagem de tempo é contínua entre os componentes. O tempo de descoberta de V4 (13) é o passo seguinte ao tempo de finalização de V6 (12), provando que o algoritmo explora todo o grafo, conforme solicitado.

---

## 4. Exemplo de Resultado Esperado: BFS em Grafo Direcionado

Para o BFS, criamos um **grafo direcionado simples** para testar a busca por níveis e o cálculo de distâncias.

### Cenário de Teste

- **Grafo**: Direcionado.
- **Ação**: Executar BFS a partir do Nó V1.

> ![Resultado Esperado do BFS](inserir-caminho-da-imagem-do-bfs-aqui)

### Análise do Resultado

- **Ordem de Visita**: A ordem V1 → V2 → V3 → V4 reflete a exploração por níveis, uma característica fundamental do BFS.

#### Tabela de Resultados

- **Distância**: Os valores mostram a menor quantidade de arestas a partir do nó inicial V1. A distância para V4 é 2 (caminho V1 → V2 → V4), o que está correto.
- **Pai**: A tabela de pais reflete corretamente o caminho mais curto encontrado pelo BFS.
