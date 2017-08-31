from Banco import Banco
from tkinter import *
from tkinter import messagebox


from Filmes import Filmes

banco = Banco()


class main:
    def __init__(self,master):
        #Variavel para genero
        self.variablegen = StringVar(master)

        self.container1 = Frame(master)
        self.container1.grid(row=0,column=0)


        #Botão de adicionar
        self.btnaddnovo = Button(self.container1, text = "Adicionar filme", command=self.topLevelAddFilme)
        self.btnaddnovo.grid(row=0,column=0)


        #Botão buscar
        self.btnbuscarnovo = Button(self.container1, text = "Buscar filme")
        self.btnbuscarnovo.grid(row=0,column=1)




    def adicionarFilmeTop(self):
        nome = self.afed1.get()
        sinopse = self.afed2.get()
        genero = self.variablegen.get()
        ano = self.afed4.get()
        if nome != "" and sinopse != "" and genero != "" and ano != "":
            filme = Filmes(nome, sinopse, genero, ano)
            try:
                banco.addFilme(filme)
                messagebox.showinfo("Log", "Filme adicionado ao estoque")
            except:
                messagebox.showinfo("Log", "Ocorreu um erro ao adicionar")
        else:
            messagebox.showinfo("Log", "Preencha todos os campos")





    #Adicionar Filme
    def topLevelAddFilme(self): #Abrir janela para cadastrar filme
        top = Toplevel()
        top.title("Novo filme")
        top.geometry("250x400+100+100")
        top['bg'] = 'blue'


        self.aflbl0 = Label(top, text = "Adicionar filme",font = ("Verdana", "10",  "bold",), bg = 'blue', fg = 'white')
        self.aflbl0.grid(row=0,column=1)

        self.aflb1 = Label(top, text="Nome", font =  ("Calibri", "12"), bg = 'blue',  fg = 'white')
        self.aflb1.grid(row=1, sticky=W)

        self.afed1 = Entry(top)
        self.afed1.grid(row=1, column=1)

        self.aflb2 = Label(top, text="Sinopse", font =  ("Calibri", "12"), bg = 'blue',  fg = 'white')
        self.aflb2.grid(row=2, sticky=W)

        self.afed2 = Entry(top)
        self.afed2.grid(row=2, column=1)

        self.aflb3 = Label(top, text="Genero", font =  ("Calibri", "12"), bg = 'blue',  fg = 'white')
        self.aflb3.grid(row=3, sticky=W)

        lst = ["Terror", "Ação", "Comédia", "Aventura", "Esportes", "Drama", "Documentário", "Animação"]
        self.variablegen.set("Comédia")


        self.afed3 = OptionMenu(top,self.variablegen,*lst)    #Entrada de genero de filme
        self.afed3['width'] = 13
        self.afed3['borderwidth'] = 2
        self.afed3.grid(row=3, column=1)

        self.aflb4 = Label(top, text="Lançamento", font =  ("Calibri", "12"), bg = 'blue',  fg = 'white')
        self.aflb4.grid(row=4, sticky=W)

        self.afed4 = Entry(top)
        self.afed4.grid(row=4, column=1)


        self.afbtnok = Button(top, text="Adicionar", command=  self.adicionarFilmeTop)
        self.afbtnok.grid(row=5,column=1)













































root = Tk()
root.wm_title("Sistema Locadora")
root.geometry("900x600+100+100")
main(root)
root.mainloop()