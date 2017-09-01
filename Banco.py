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
    """) #Tabela criada
        self.con.commit()
        c.close()

    def addFilme(self, filme): #Adiciona um filme, é passado como argumento um objeto do tipo Filmes.
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


    def updateFilme(self, id, nome, sinopse, genero, datadelancamento): #Atualiza o filme com base no id
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

    def deleteFilme(self, id): #Deleta o filme com base no id
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

    def getFilmeId(self,id): #Gera uma lista de filmes com base em um id específico, a lista contém todas as informações do filme.
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

    def getFilmeNome(self,nome): #Gera uma lista de filmes com base em um nome especifico, a lista contém id e nome.
        try:
            lista = []
            c = self.con.cursor()
            c.execute("""
            SELECT * FROM estoque WHERE nome = ?
            """,(nome,))
            for linha in c:
                lista.append([linha[0],linha[1]])
            self.con.commit()
            c.close()

            if lista != []:
                return lista
            else:
                return ''
        except:
            return ''


    def getFilmeGenero(self,genero): #Gera uma lista de filme com base em um gênero específico, a lista contém id e nome.
        if genero != 'Todos':
            try:
                lista = []
                c = self.con.cursor()
                c.execute("""
                SELECT * FROM estoque WHERE genero = ? ORDER BY nome
                """,(genero,))
                for linha in c:
                    lista.append([linha[0], linha[1]])
                if lista != []:
                    return lista
                else:
                    return ""
            except:
                return "Erro"
        else:
            try:
                lista = []
                c = self.con.cursor()
                c.execute("""
                                SELECT * FROM estoque ORDER BY nome
                                """)
                for linha in c:
                    lista.append([linha[0], linha[1]])
                if lista != []:
                    return lista
                else:
                    return ""
            except:
                return "Erro"
























