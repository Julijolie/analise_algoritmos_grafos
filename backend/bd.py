# Grafo 1 (Não-Direcionado) da imagem do PDF 
grafo_nao_direcionado = {
    "A": ["B", "E"],
    "B": ["A", "C", "E"],
    "C": ["B", "F"],
    "D": ["E", "G", "H"],
    "E": ["A", "B", "D", "F"],
    "F": ["C", "E", "I"],
    "G": ["D", "H"],
    "H": ["D", "G"],
    "I": ["F"]
}

# Grafo 2 (Direcionado) da imagem do PDF 
grafo_direcionado = {
    "A": ["B", "F"],
    "B": ["D"],
    "C": ["D", "H"],
    "D": ["H"],
    "E": ["B", "G"],
    "F": ["E", "G"],
    "G": ["F"],
    "H": []
}

# Um dicionário para mapear IDs aos nossos grafos
grafos_disponiveis = {
    "nao_direcionado": {
        "nome": "Grafo 1 - Não-Direcionado",
        "estrutura": grafo_nao_direcionado
    },
    "direcionado": {
        "nome": "Grafo 2 - Direcionado",
        "estrutura": grafo_direcionado
    }
}

# --- Funções de Busca Aprimoradas ---

def bfs(grafo, inicio):
    visitados = []
    fila = [inicio]
    distancia = {node: float('inf') for node in grafo}
    pai = {node: None for node in grafo}

    distancia[inicio] = 0
    
    ordem_visita = []

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)
            ordem_visita.append(vertice)
            
            for vizinho in grafo.get(vertice, []):
                if vizinho not in visitados:
                    distancia[vizinho] = distancia[vertice] + 1
                    pai[vizinho] = vertice
                    fila.append(vizinho)
                    
    return {
        "ordem_visita": ordem_visita,
        "distancias": distancia,
        "pais": pai
    }


tempo = 0
def dfs(grafo, inicio):
    visitados = []
    pai = {node: None for node in grafo}
    tempo_descoberta = {node: 0 for node in grafo}
    tempo_finalizacao = {node: 0 for node in grafo}
    global tempo
    tempo = 0

    # Inicia a busca a partir do vértice inicial
    if inicio in grafo:
        _dfs_visit(grafo, inicio, visitados, pai, tempo_descoberta, tempo_finalizacao)

    # Garante que todos os nós sejam visitados (para grafos desconexos)
    for vertice in grafo:
        if vertice not in visitados:
            _dfs_visit(grafo, vertice, visitados, pai, tempo_descoberta, tempo_finalizacao)

    return {
        "ordem_visita": visitados,
        "pais": pai,
        "tempo_descoberta": tempo_descoberta,
        "tempo_finalizacao": tempo_finalizacao
    }

def _dfs_visit(grafo, vertice, visitados, pai, tempo_descoberta, tempo_finalizacao):
    global tempo
    tempo += 1
    tempo_descoberta[vertice] = tempo
    visitados.append(vertice)

    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            pai[vizinho] = vertice
            _dfs_visit(grafo, vizinho, visitados, pai, tempo_descoberta, tempo_finalizacao)

    tempo += 1
    tempo_finalizacao[vertice] = tempo