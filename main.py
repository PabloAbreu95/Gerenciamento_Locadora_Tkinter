from Banco import Banco
from tkinter import *
from tkinter import messagebox

#Programa para gerenciamento de uma locadora
from Filmes import Filmes
from Clientes import Clientes
from BancoClientes import BancoClientes

banco = Banco()
banco2 = BancoClientes()


class main:
    def __init__(self,master):
        #Variavel para genero
        self.variablegen = StringVar(master)
        self.variablegen2 = StringVar(master) #Buscar filme(gênero)

        #Label Inicial
        self.lb1 = Label(master,text="Sistema Automatizado Locadora", font = ('Calibri' ,'15','bold'))
        self.lb1.pack()


        #Botão de adicionar
        self.btnaddnovo = Button(master, text = "Adicionar filme", command=self.topLevelAddFilme, width=25, font = ('Arial' ,10))
        self.btnaddnovo.pack()


        #Botão buscar
        self.btnbuscarnovo = Button(master, text = "Buscar filme", command = self.topLevelBuscarFilme, width=25, font = ('Arial' ,10))
        self.btnbuscarnovo.pack()

        #Botão de adição de clientes
        self.btncadastrarcliente = Button(master, text = "Adicionar cliente", command = self.topLevelClientes, width=25, font = ('Arial' ,10))
        self.btncadastrarcliente.pack()

        #Botão de busca de clientes
        self.btnbuscarclientes = Button(master, text = 'Buscar clientes', font = ('Arial',10), width=25, command = self.topLevelBuscarClientes)
        self.btnbuscarclientes.pack()



    def adicionarFilmeTop(self): #Função que checa possíveis erros e adiciona filme
        nome = self.afed1.get()
        sinopse = self.afed2.get()
        genero = self.variablegen.get()
        ano = self.afed4.get()
        if nome != "" and sinopse != "" and genero != "" and ano != "":
            if banco.getFilmeNome(nome) != True:
                filme = Filmes(nome, sinopse, genero, ano)
                banco.addFilme(filme)
                messagebox.showinfo("Log", "Filme adicionado ao estoque")
            else:
                result = messagebox.askquestion("Atenção", "Há um filme com esse mesmo nome no estoque, deseja adicionar?", icon = "warning")
                if(result == "yes"):
                    filme = Filmes(nome, sinopse, genero, ano)
                    try:
                        banco.addFilme(filme)
                        messagebox.showinfo("Log", "Filme adicionado ao estoque")
                    except:
                        messagebox.showinfo("Log", "Ocorreu um erro ao adicionar")
                else:
                    messagebox.showinfo("Log", "Filme não adicionado")
        else:
            messagebox.showinfo("Log", "Preencha todos os campos")

    def refresh(self, event):  #Atualiza o listbox da busca de filmes
        if self.bfed1.get() == '':
            lst = banco.getFilmeGenero(self.variablegen2.get())
            self.bflbox1.delete(0, END) #Limpa a listbox
            for item in lst: #Preenche com novos
                self.bflbox1.insert(END, item)
        else:
            lst = banco.getFilmeNome(self.bfed1.get())
            self.bflbox1.delete(0, END)
            for item in lst:
                self.bflbox1.insert(END, item)


    #Adicionar Filme
    def topLevelAddFilme(self): #Janela top level criada(cadastro de filmes)
        top = Toplevel()
        top.title("Novo filme")
        top.geometry("250x200+100+100")
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


    def topLevelBuscarFilme(self):  #Janela TOP-LEVEL criada(busca de filmes)
        top2 = Toplevel()
        top2.title('Buscar Filme')
        top2.geometry("300x250+100+100")


        self.bflb0 = Label(top2, text='Buscar Filme', font = ("Verdana", "10",  "bold"))
        self.bflb0.grid(row=0, column=1)

        self.bflb1 = Label(top2, text='Nome', font =  ("Calibri", "12"))
        self.bflb1.grid(row=1, sticky=W)

        self.bfed1 = Entry(top2)
        self.bfed1.grid(row=1, column=1)

        self.bfbt1 = Button(top2, text='Buscar')
        self.bfbt1.bind("<Button-1>", self.refresh)
        self.bfbt1.grid(row=1, column=2)

        self.bflb2 = Label(top2, text='Gênero', font =  ("Calibri", "12"))
        self.bflb2.grid(row=2, column=0)

        lst2 = ["Todos", "Terror", "Ação", "Comédia", "Aventura", "Esportes", "Drama", "Documentário", "Animação"]
        self.variablegen2.set("Todos")
        self.bfop1 = OptionMenu(top2,self.variablegen2,*lst2)
        self.bfop1['width'] = 13
        self.bfop1['borderwidth'] = 2
        self.bfop1.grid(row=2, column=1)




        self.bflbox1 = Listbox(top2)
        lst3 = banco.getFilmeGenero(self.variablegen2.get())
        print(lst3)
        for item in lst3:
            self.bflbox1.insert(END, item)
        self.bflbox1.grid(row=3, column=1)

    #Função para adicionar cliente
    def adicionarCliente(self):
        try:
            cliente = Clientes(self.ced1.get(), self.ced2.get(), self.ced3.get(),self.ced4.get(),self.ced5.get(),self.ced6.get(), self.ced7.get())
            if(cliente.nome != "" and cliente.cpf != "" and cliente.telefone != "" and\
               cliente.email != "" and cliente.endereco != "" and cliente.numero != "" and cliente.bairro != ""):
                if(cliente.validarCPF() and cliente.validarNome()):
                    if(banco2.checkCpf(cliente.cpf) == True): #Checa se já existe uma ocorrência
                        banco2.addCliente(cliente)
                        messagebox.showinfo("Log", "Cliente adicionado com sucesso!")
                        self.ced1.delete(0, END)
                        self.ced2.delete(0, END)
                        self.ced3.delete(0, END)
                        self.ced4.delete(0, END)
                        self.ced5.delete(0, END)
                        self.ced6.delete(0, END)
                        self.ced7.delete(0, END)
                        print(cliente.cpf)
                    else:
                        messagebox.showinfo("Log", "CPF já cadastrado!")
                else:
                    messagebox.showinfo("Log", "Dados inválidos!")
            else:
                messagebox.showinfo("Log", "Preenncha todos os campos!")
        except:
            messagebox.showinfo("Log", "Erro ao adicionar cliente!")

    def topLevelClientes(self):
        top3 = Toplevel()
        top3.geometry("250x250+600+100")

        self.clb1 = Label(top3,text='Adicionar cliente',font = ("Verdana", "10",  "bold"))
        self.clb1.grid(row=0, column=1)

        self.clb2 = Label(top3, text='NOME', font =  ("Calibri", "12"))
        self.clb2.grid(row=1, column=0)

        self.ced1 = Entry(top3) #Entry de nome
        self.ced1.grid(row=1, column=1)

        self.clb2 = Label(top3, text='CPF', font =  ("Calibri", "12"))
        self.clb2.grid(row=2, column=0)

        self.ced2 = Entry(top3) #Entry de cpf
        self.ced2.grid(row=2, column=1)

        self.clb3 = Label(top3, text='TELEFONE')
        self.clb3.grid(row=3,column=0)

        self.ced3 = Entry(top3) #Entry de telefone
        self.ced3.grid(row=3,column=1)

        self.clb4 = Label(top3, text='EMAIL')
        self.clb4.grid(row=4, column=0)

        self.ced4 = Entry(top3) #Entry de email
        self.ced4.grid(row=4, column=1)

        self.clb5 = Label(top3, text='ENDEREÇO')
        self.clb5.grid(row=5, column=0)

        self.ced5 = Entry(top3)  # Entry de endereço
        self.ced5.grid(row=5, column=1)

        self.clb6 = Label(top3, text='NÚMERO')
        self.clb6.grid(row=6, column=0)

        self.ced6 = Entry(top3)  # Entry de Numero
        self.ced6.grid(row=6, column=1)

        self.clb7 = Label(top3, text='BAIRRO')
        self.clb7.grid(row=7, column=0)

        self.ced7 = Entry(top3)  # Entry de email
        self.ced7.grid(row=7, column=1)

        self.cbtn2 = Button(top3, text='Salvar', width=10, command=self.adicionarCliente)
        self.cbtn2.grid(row=8,column=1)

    def realizarBusca(self):
        try:
            cpf = self.bced1.get()
            if(banco2.checkCpf(cpf) == False):
                lista = banco2.buscarCpf(cpf)
                self.bced2.insert(0, lista[1]) #Nome
                self.bced3.insert(0, lista[3]) #Telefone
                self.bced4.insert(0, lista[4]) #Email
                self.bced5.insert(0, lista[5]) #Endereço
                self.bced6.insert(0, lista[6]) #Número
                self.bced7.insert(0, lista[7]) #Bairro
                self.bced8.insert(0, lista[0]) #Id
            else:
                messagebox.showinfo("Log", "Cpf não cadastrado")
        except:
            print('Erro')

    def excluirCliente(self):
        try:
            id = self.bced8.get()
            banco2.deleteCliente(id)
            messagebox.showinfo("Log", "Cliente removido")
            self.bced1.delete(0, END)
            self.bced2.delete(0, END)
            self.bced3.delete(0, END)
            self.bced4.delete(0, END)
            self.bced5.delete(0, END)
            self.bced6.delete(0, END)
            self.bced7.delete(0, END)
            self.bced8.delete(0, END)
        except:
            print('Erro')

    def alterarCliente(self):
        try:
            id = self.bced8.get()
            nome = self.bced2.get()
            telefone = self.bced3.get()
            email = self.bced4.get()
            endereco = self.bced5.get()
            numero = self.bced6.get()
            bairro = self.bced7.get()
            cpf = ""
            cliente = Clientes(nome,cpf,telefone,email,endereco,numero,bairro)
            banco2.updateCliente(id,cliente)
            messagebox.showinfo("Log", "Cliente alterado com sucesso!")
        except:
            messagebox.showinfo("Log", "Erro ao alterar cliente!")



    def topLevelBuscarClientes(self):
        top4 = Toplevel()
        top4.geometry("250x250+600+100")

        self.bclb1 = Label(top4, text = 'Busca de cliente', font = ("Verdana", "10",  "bold"))
        self.bclb1.grid(row=0, column=1)

        self.bclb2 = Label(top4, text='CPF', font=('Calibri','10'))
        self.bclb2.grid(row=1,column=0)

        self.bced1 = Entry(top4) #Entry do cpf
        self.bced1.grid(row=1,column=1)

        self.bcbt1 = Button(top4, text='Buscar', font=('Calibri',10), command = self.realizarBusca)
        self.bcbt1.grid(row=1, column=2)

        self.bclb3 = Label(top4, text='NOME', font=('Calibri', '10'))
        self.bclb3.grid(row=2, column=0)

        self.bced2 = Entry(top4)  # Entry do nome
        self.bced2.grid(row=2, column=1)

        self.bclb4 = Label(top4, text='TELEFONE', font=('Calibri', '10'))
        self.bclb4.grid(row=3, column=0)

        self.bced3 = Entry(top4)  # Entry do telefone
        self.bced3.grid(row=3, column=1)

        self.bclb5 = Label(top4, text='EMAIL', font=('Calibri', '10'))
        self.bclb5.grid(row=4, column=0)

        self.bced4 = Entry(top4)  # Entry do Email
        self.bced4.grid(row=4, column=1)

        self.bclb6 = Label(top4, text='ENDEREÇO', font=('Calibri', '10'))
        self.bclb6.grid(row=5, column=0)

        self.bced5 = Entry(top4)  # Entry do endereco
        self.bced5.grid(row=5, column=1)

        self.bclb7 = Label(top4, text='NÚMERO', font=('Calibri', '10'))
        self.bclb7.grid(row=6, column=0)

        self.bced6 = Entry(top4)  # Entry do numero
        self.bced6.grid(row=6, column=1)

        self.bclb8 = Label(top4, text='BAIRRO', font=('Calibri', '10'))
        self.bclb8.grid(row=7, column=0)

        self.bced7 = Entry(top4)  # Entry do bairro
        self.bced7.grid(row=7, column=1)

        self.bclb9 = Label(top4, text='ID', font=('Calibri', '10'))
        self.bclb9.grid(row=8, column=0)

        self.bced8 = Entry(top4)  # Entry do bairro
        self.bced8.grid(row=8, column=1)

        self.bcbtn2 = Button(top4, text = 'Alterar', command=self.alterarCliente)
        self.bcbtn2.grid(row=9, column=1)

        self.bcbtn3= Button(top4, text='Excluir', command=self.excluirCliente)
        self.bcbtn3.grid(row=9, column=0)
































































root = Tk()
root.wm_title("Sistema Locadora")
root.geometry("300x300+100+100")
main(root)
root.mainloop()
