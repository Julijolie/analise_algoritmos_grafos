# app.py
from flask import Flask, request, jsonify
from bd import bfs, dfs, grafos_disponiveis  # Importamos os grafos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

@app.route('/')
def home():
    return "API de Grafos rodando com sucesso!"

# NOVA ROTA: Retorna os grafos disponíveis para o frontend
@app.route('/grafos', methods=['GET'])
def get_grafos():
    # Retorna um dicionário mais simples, sem a estrutura interna, para o frontend escolher
    info_grafos = {id: {"nome": detalhes["nome"], "nos": list(detalhes["estrutura"].keys())} for id, detalhes in grafos_disponiveis.items()}
    return jsonify(info_grafos)

def executar_algoritmo(algoritmo_func):
    dados = request.get_json()
    id_grafo = dados.get("id_grafo")
    inicio = dados.get("inicio")

    if not id_grafo or not inicio:
        return jsonify({"erro": "ID do grafo ou vértice inicial ausente"}), 400

    # Busca o grafo pela ID em nosso "banco de dados"
    grafo_info = grafos_disponiveis.get(id_grafo)
    if not grafo_info:
        return jsonify({"erro": f"Grafo com ID '{id_grafo}' não encontrado"}), 404
        
    grafo = grafo_info["estrutura"]

    # Verifica se o nó inicial existe no grafo selecionado
    if inicio not in grafo:
        return jsonify({"erro": f"Vértice inicial '{inicio}' não existe no grafo selecionado"}), 400

    resultado = algoritmo_func(grafo, inicio)
    return jsonify({"algoritmo": algoritmo_func.__name__.upper(), "resultado": resultado})

@app.route('/bfs', methods=['POST'])
def executar_bfs():
    return executar_algoritmo(bfs)

@app.route('/dfs', methods=['POST'])
def executar_dfs():
    return executar_algoritmo(dfs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)