from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)