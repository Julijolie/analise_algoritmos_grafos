# backend/app.py
from flask import Flask, request, jsonify
from bd import bfs, dfs  # Importa apenas as funções de busca
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- Função Auxiliar ---
def converter_cy_para_adj(graph_data, is_directed=True):
    """Converte dados do formato Cytoscape.js para uma lista de adjacência."""
    adj_list = {}
    nodes = graph_data.get('nodes', [])
    edges = graph_data.get('edges', [])

    # 1. Inicializa a lista de adjacência com todos os nós (vértices)
    for node_data in nodes:
        node_id = node_data.get('data', {}).get('id')
        if node_id:
            adj_list[node_id] = []

    # 2. Preenche a lista com as arestas
    for edge_data in edges:
        source = edge_data.get('data', {}).get('source')
        target = edge_data.get('data', {}).get('target')
        if source in adj_list and target in adj_list:
            adj_list[source].append(target)
            # Se o grafo não for direcionado, adiciona a aresta de volta
            if not is_directed:
                adj_list[target].append(source)
    return adj_list

# --- Rota Principal da API ---

@app.route('/')
def home():
    return "API de Algoritmos de Grafos pronta para receber dados!"

@app.route('/run-algorithm', methods=['POST'])
def run_algorithm():
    """Rota única que recebe os dados do grafo do frontend e executa o algoritmo."""
    dados = request.get_json()
    
    # Extrai os dados enviados pelo frontend
    graph_data = dados.get("graph_data")
    no_inicial = dados.get("inicio")
    tipo_algoritmo = dados.get("tipo")
    is_directed = dados.get("is_directed", True) # Assume direcionado se não especificado

    # Validação básica
    if not all([graph_data, no_inicial, tipo_algoritmo]):
        return jsonify({"erro": "Dados insuficientes para executar o algoritmo"}), 400
    
    # Converte o grafo do frontend para um formato que as funções entendem
    grafo_dict = converter_cy_para_adj(graph_data, is_directed)

    # Verifica se o nó inicial existe no grafo criado
    if no_inicial not in grafo_dict:
        return jsonify({"erro": f"Vértice inicial '{no_inicial}' não encontrado no grafo criado"}), 400

    # Escolhe a função de busca correta (bfs ou dfs)
    algoritmo_func = dfs if tipo_algoritmo == 'dfs' else bfs
    
    # Executa o algoritmo
    resultado = algoritmo_func(grafo_dict, no_inicial)
    
    # Retorna o resultado completo para o frontend
    return jsonify({
        "algoritmo": algoritmo_func.__name__.upper(),
        "no_inicial": no_inicial,
        "resultado": resultado
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
