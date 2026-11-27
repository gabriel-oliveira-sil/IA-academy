from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar python", "feito": False},
    {"id": 2, "titulo": "Estudar flask", "feito": True},
    {"id": 3, "titulo": "Estudar SQL", "feito": False},
    {"id": 4, "titulo": "Fazer exercícios", "feito": True},
]

def buscar_tarefa(tarefas, id_tarefa):
    for t in tarefas:
        if t["id"] == id_tarefa:
            return t
    return None

@app.route("/")
def inicio():
    return "API de tarefas funcionando!"

@app.route("/tarefas")
def listar_tarefas():
    return jsonify(tarefas) 

@app.route("/tarefas/<int:id_tarefa>")
def obter_tarefa(id_tarefa):
    tarefa = buscar_tarefa(tarefas, id_tarefa)
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    nova = {"id": tarefas[-1]["id"] + 1, "titulo": dados["titulo"], "feito": False}
    tarefas.append(nova)
    return jsonify(nova), 201

if __name__ == "__main__":
    app.run(debug=True)