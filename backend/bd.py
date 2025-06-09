from collections import deque

def dfs(grafo, inicio):
    """Executa a Busca em Profundidade (DFS) a partir de um nó inicial, visitando todos os componentes."""
    visitados_ordem = []
    visitados_set = set()
    previsit = {}
    postvisit = {}
    pais = {no: None for no in grafo}
    tempo = 1

    def _dfs_recursive(no):
        nonlocal tempo
        visitados_set.add(no)
        visitados_ordem.append(no)
        previsit[no] = tempo
        tempo += 1

        for vizinho in grafo.get(no, []):
            if vizinho not in visitados_set:
                pais[vizinho] = no
                _dfs_recursive(vizinho)
        
        postvisit[no] = tempo
        tempo += 1

    # Inicia a busca a partir do nó escolhido.
    if inicio in grafo:
        _dfs_recursive(inicio)
    
    # Este loop garante que, mesmo que o grafo seja desconexo, 
    # todos os nós restantes sejam visitados, continuando a contagem de tempo.
    for no in grafo:
        if no not in visitados_set:
            _dfs_recursive(no)

    return {
        "ordem_visita": visitados_ordem,
        "pais": pais,
        "tempo_descoberta": previsit,
        "tempo_finalizacao": postvisit
    }


def bfs(grafo, inicio):
    """Executa a Busca em Largura (BFS) a partir de um nó inicial, visitando todos os componentes."""
    ordem_visita = []
    visitados_set = set()
    distancia = {no: float('inf') for no in grafo}
    pai = {no: None for no in grafo}
    
    def _bfs_componente(no_inicial_componente):
        if no_inicial_componente in visitados_set:
            return

        fila = deque([no_inicial_componente])
        visitados_set.add(no_inicial_componente)
        distancia[no_inicial_componente] = 0
        
        while fila:
            atual = fila.popleft()
            ordem_visita.append(atual)

            for vizinho in grafo.get(atual, []):
                if vizinho not in visitados_set:
                    visitados_set.add(vizinho)
                    pai[vizinho] = atual
                    distancia[vizinho] = distancia[atual] + 1
                    fila.append(vizinho)

    # Inicia a busca pelo componente do nó escolhido
    _bfs_componente(inicio)

    # Continua a busca por outros componentes desconexos
    for no in grafo:
        if no not in visitados_set:
            _bfs_componente(no)

    return {
        "ordem_visita": ordem_visita,
        "distancias": distancia,
        "pais": pai
    }
