from flask import Flask
from controller.filme_controller import FilmeController

app = Flask(__name__)


@app.route("/filmes", methods=["GET"])
def consultar_filmes():
    return FilmeController.consultar_todos()


@app.route("/filmes/<int:id>", methods=["GET"])
def consultar_filme_por_id(id):
    return FilmeController.consultar_por_id(id)


@app.route("/filmes", methods=["POST"])
def cadastrar_filme():
    return FilmeController.cadastrar()


@app.route("/filmes/<int:id>", methods=["PUT"])
def atualizar_filme(id):
    return FilmeController.atualizar(id)


@app.route("/filmes/<int:id>", methods=["DELETE"])
def excluir_filme(id):
    return FilmeController.excluir(id)


if __name__ == "__main__":
    app.run(debug=True)
