from flask import Flask, request, jsonify
from bd import bfs, dfs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API de Grafos rodando com sucesso!"

@app.route('/bfs', methods=['POST'])
def executar_bfs():
    dados = request.get_json()
    grafo = dados.get("grafo")
    inicio = dados.get("inicio")
    
    if not grafo or not inicio:
        return jsonify({"erro": "grafo ou vértice inicial ausente"}), 400

    resultado = bfs(grafo, inicio)
    return jsonify({"algoritmo": "BFS", "resultado": resultado})

@app.route('/dfs', methods=['POST'])
def executar_dfs():
    dados = request.get_json()
    grafo = dados.get("grafo")
    inicio = dados.get("inicio")

    if not grafo or not inicio:
        return jsonify({"erro": "grafo ou vértice inicial ausente"}), 400

    resultado = dfs(grafo, inicio)
    return jsonify({"algoritmo": "DFS", "resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)
