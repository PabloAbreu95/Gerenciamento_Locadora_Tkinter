import sqlite3
class Banco:
    def __init__(self):
        #Criando conexão
        con = sqlite3.connect('filmes.db')
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