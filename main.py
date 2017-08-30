from Filmes import Filmes
from Banco import Banco
from tkinter import *
from functools import partial
import tkinter
import tkinter.messagebox

banco = Banco()





class main:
    def __init__(self,master):
        self.container1 = Frame(master)
        self.container1.grid(row=0,column=0)

        #Botão de adicionar
        self.btnaddnovo = Button(self.container1, text = "Adicionar Filme", command=self.topLevelAddFilme)
        self.btnaddnovo.grid(row=0,column=0)




    #Funções
    def topLevelAddFilme(self): #Abrir janela para cadastrar filme
        top = Toplevel()
        top.title("Novo filme")
        top.geometry("250x200+100+100")


        self.aflbl0 = Label(top, text = "Adicionar filme")
        self.aflbl0.grid(row=0,column=1)

        top.aflb1 = Label(top, text="Nome")
        top.aflb1.grid(row=1, sticky=W)

        top.afed1 = Entry(top)
        top.afed1.grid(row=1, column=1)

        top.aflb2 = Label(top, text="Sinopse")
        top.aflb2.grid(row=2, sticky=W)

        top.afed2 = Entry(top)
        top.afed2.grid(row=2, column=1)

        top.aflb3 = Label(top, text="Genero")
        top.aflb3.grid(row=3, sticky=W)

        top.afed3 = Entry(top)
        top.afed3.grid(row=3, column=1)

        top.aflb4 = Label(top, text="Lançamento")
        top.aflb4.grid(row=4, sticky=W)

        top.afed4 = Entry(top)
        top.afed4.grid(row=4, column=1)


        top.afbtnok = Button(top, text="Adicionar")
        top.afbtnok.grid(row=5,column=1)
        aflb5 = Label(top, text ="x")
        aflb5.grid(row=6, column=1)





































root = Tk()
root.wm_title("Sistema Locadora")
root.geometry("900x600+100+100")
main(root)
root.mainloop()