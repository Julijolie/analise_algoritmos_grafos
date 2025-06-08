# backend/app.py
from flask import Flask, request, jsonify
from bd import grafos_disponiveis, bfs, dfs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API de Grafos rodando com sucesso!"

def formatar_para_cytoscape(grafo_dict, is_directed):
    """Converte a lista de adjacência para o formato do Cytoscape.js, evitando arestas duplicadas em grafos não-direcionados."""
    elementos = []
    # Adiciona os nós
    for no in grafo_dict.keys():
        elementos.append({"data": {"id": no}})
    
    arestas_adicionadas = set()
    for no, vizinhos in grafo_dict.items():
        for vizinho in vizinhos:
            if is_directed:
                # Em grafos direcionados, simplesmente adiciona a aresta
                elementos.append({"data": {"source": no, "target": vizinho}})
            else:
                # Em grafos não-direcionados, cria uma chave única para a aresta (ordenada)
                # para evitar adicionar tanto A-B quanto B-A.
                edge_key = "-".join(sorted((no, vizinho)))
                if edge_key not in arestas_adicionadas:
                    elementos.append({"data": {"source": no, "target": vizinho}})
                    arestas_adicionadas.add(edge_key)
    return elementos

@app.route('/grafos', methods=['GET'])
def get_grafos():
    """Retorna dados do grafo, incluindo o formato para o Cytoscape."""
    info_grafos = {}
    for id, grafo_info in grafos_disponiveis.items():
        is_directed = "direcionado" in id
        info_grafos[id] = {
            "nome": grafo_info["nome"],
            "nos": list(grafo_info["estrutura"].keys()),
            "estrutura_adj": grafo_info["estrutura"],
            "elementos_cy": formatar_para_cytoscape(grafo_info["estrutura"], is_directed)
        }
    return jsonify(info_grafos)

def executar_algoritmo(algoritmo_func):
    dados = request.get_json()
    id_grafo = dados.get("id_grafo")
    no_inicial = dados.get("inicio")

    if not id_grafo or not no_inicial:
        return jsonify({"erro": "ID do grafo ou vértice inicial ausente"}), 400

    grafo_info = grafos_disponiveis.get(id_grafo)
    if not grafo_info:
        return jsonify({"erro": f"Grafo com ID '{id_grafo}' não encontrado"}), 404
    
    grafo_dict = grafo_info["estrutura"]
        
    if no_inicial not in grafo_dict:
        return jsonify({"erro": f"Vértice inicial '{no_inicial}' não existe no grafo selecionado"}), 400

    # Chama a função de busca diretamente, passando o grafo como argumento
    resultado = algoritmo_func(grafo_dict, no_inicial)
        
    return jsonify({
        "algoritmo": algoritmo_func.__name__.upper(),
        "no_inicial": no_inicial,
        "resultado": resultado
    })

@app.route('/bfs', methods=['POST'])
def executar_bfs():
    return executar_algoritmo(bfs)

@app.route('/dfs', methods=['POST'])
def executar_dfs():
    return executar_algoritmo(dfs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
