# bd.py

def bfs(grafo, inicio):
    visitados = []
    fila = [inicio]

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)
            fila.extend([vizinho for vizinho in grafo.get(vertice, []) if vizinho not in visitados])
    return visitados

def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = []

    if inicio not in visitados:
        visitados.append(inicio)
        for vizinho in grafo.get(inicio, []):
            dfs(grafo, vizinho, visitados)

    return visitados
