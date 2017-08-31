import sqlite3

class Banco:
    def __init__(self):
        #Criando conexão
        self.con = sqlite3.connect('filmes.db')
        self.createTable()

    def createTable(self):
        #Criando um cursor
        c = self.con.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS estoque(
          id INTEGER NOT NULL PRIMARY KEY,
          nome TEXT,
          sinopse TEXT,
          genero TEXT,
          datadelancamento TEXT
        );
    """)
        self.con.commit()
        c.close()

    def addFilme(self, filme):
        try:
            c = self.con.cursor()
            c.execute("""
               INSERT INTO estoque(nome, sinopse, genero, datadelancamento) VALUES (?,?,?,?)
               """, (filme.nome, filme.sinopse, filme.genero, filme.datadelancamento))
            self.con.commit()
            c.close()
            return "Filme adicionado ao estoque com sucesso!"

        except:
            return "Ocorreu um erro ao adicionar o filme"


    def updateFilme(self, id, nome, sinopse, genero, datadelancamento):
        try:
            c = self.con.cursor()
            c.execute("""
            UPDATE estoque
            SET nome = ?,  sinopse = ?, genero = ?, datadelancamento = ? WHERE  id = ?
            """, (nome, sinopse, genero, datadelancamento, id,))
            self.con.commit()
            c.close()
            return "Filme atualizdo com sucesso"
        except:
            return "Ocorreu um erro ao atualizar o filme"

    def deleteFilme(self, id):
        try:
            c = self.con.cursor()
            c.execute("""
            DELETE FROM estoque WHERE id = ?
            """,(id,))
            self.con.commit()
            c.close()
            print("sucesso")
            return "Filme removido com sucesso!"
        except:
            print('falha')
            return "Erro ao remover filme!"

    def getFilmeIp(self,id):
        try:
            lista = []
            c = self.con.cursor()
            c.execute("""
            SELECT * FROM estoque WHERE id = ?
            """,(id,))
            for linha in c:
                lista.append(linha)
            if lista != []:
                return lista
            else:
                return "Id não encontrado"
        except:
            return "Erro"
