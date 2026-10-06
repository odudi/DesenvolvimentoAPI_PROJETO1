from config.conexao import get_connection


class Filme:

    @staticmethod
    def consultar_todos():
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM Filmes"
        cursor.execute(sql)

        filmes = cursor.fetchall()

        cursor.close()
        conexao.close()

        return filmes

    @staticmethod
    def consultar_por_id(id):
        conexao = get_connection()
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM Filmes WHERE id = %s"
        cursor.execute(sql, (id,))

        filme = cursor.fetchone()

        cursor.close()
        conexao.close()

        return filme

    @staticmethod
    def cadastrar(dados):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO Filmes
            (titulo, diretor, genero, ano, duracao, nota)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            dados["titulo"],
            dados["diretor"],
            dados["genero"],
            dados["ano"],
            dados["duracao"],
            dados["nota"]
        )

        cursor.execute(sql, valores)
        conexao.commit()

        id_novo_filme = cursor.lastrowid

        cursor.close()
        conexao.close()

        return id_novo_filme

    @staticmethod
    def atualizar(id, dados):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = """
            UPDATE Filmes
            SET titulo = %s,
                diretor = %s,
                genero = %s,
                ano = %s,
                duracao = %s,
                nota = %s
            WHERE id = %s
        """

        valores = (
            dados["titulo"],
            dados["diretor"],
            dados["genero"],
            dados["ano"],
            dados["duracao"],
            dados["nota"],
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        linhas_alteradas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_alteradas

    @staticmethod
    def excluir(id):
        conexao = get_connection()
        cursor = conexao.cursor()

        sql = "DELETE FROM Filmes WHERE id = %s"

        cursor.execute(sql, (id,))
        conexao.commit()

        linhas_excluidas = cursor.rowcount

        cursor.close()
        conexao.close()

        return linhas_excluidas
