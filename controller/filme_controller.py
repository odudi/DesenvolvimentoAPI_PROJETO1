from flask import jsonify, request
from model.filme import Filme


class FilmeController:

    @staticmethod
    def consultar_todos():
        filmes = Filme.consultar_todos()

        for filme in filmes:
            filme["nota"] = float(filme["nota"])

        return jsonify(filmes), 200

    @staticmethod
    def consultar_por_id(id):
        filme = Filme.consultar_por_id(id)

        if filme is None:
            return jsonify({"mensagem": "Filme não encontrado"}), 404

        filme["nota"] = float(filme["nota"])

        return jsonify(filme), 200

    @staticmethod
    def cadastrar():
        dados = request.get_json()

        id_novo = Filme.cadastrar(dados)

        return jsonify({
            "mensagem": "Filme cadastrado com sucesso",
            "id": id_novo
        }), 201

    @staticmethod
    def atualizar(id):
        dados = request.get_json()

        resultado = Filme.atualizar(id, dados)

        if resultado == 0:
            return jsonify({"mensagem": "Filme não encontrado"}), 404

        return jsonify({
            "mensagem": "Filme atualizado com sucesso"
        }), 200

    @staticmethod
    def excluir(id):
        resultado = Filme.excluir(id)

        if resultado == 0:
            return jsonify({"mensagem": "Filme não encontrado"}), 404

        return jsonify({
            "mensagem": "Filme excluído com sucesso"
        }), 200
