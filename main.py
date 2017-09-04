from Banco import Banco
from tkinter import *
from tkinter import messagebox

#Programa para gerenciamento de uma locadora
from Filmes import Filmes
from Clientes import Clientes
from Pedidos import Pedidos
from BancoClientes import BancoClientes
from BancoPedidos import BancoPedidos

banco = Banco()
banco2 = BancoClientes()
banco3 = BancoPedidos()


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
    def topLevelAddFilme(self): #Janela top level criada(cadastro de filmes)  Pronto
        top = Toplevel()
        top.title("Novo filme")
        fontpadrao = ('Verdana',8)

        #Containers

        self.container0 = Frame(top)
        self.container0['pady'] = 10
        self.container0.pack()

        self.container1 = Frame(top)
        self.container1['padx'] = 15
        self.container1['pady'] = 5
        self.container1.pack()

        self.container2 = Frame(top)
        self.container2['padx'] = 15
        self.container2['pady'] = 5
        self.container2.pack()

        self.container3 = Frame(top)
        self.container3['padx'] = 15
        self.container3['pady'] = 5
        self.container3.pack()

        self.container4 = Frame(top)
        self.container4['padx'] = 15
        self.container4['pady'] = 5
        self.container4.pack()

        self.container5 = Frame(top)
        self.container5['padx'] = 15
        self.container5['pady'] = 10
        self.container5.pack()


        self.aflbl0 = Label(self.container0, text = "Adicionar filme",font = ("Calibri", "13", "bold"))
        self.aflbl0.pack()

        self.aflb1 = Label(self.container1, text="Nome", font =  fontpadrao, width=10)
        self.aflb1.pack(side=LEFT)

        self.afed1 = Entry(self.container1)
        self.afed1.pack(side=RIGHT)

        self.aflb2 = Label(self.container2, text="Sinopse", font =  fontpadrao, width=10)
        self.aflb2.pack(side=LEFT)

        self.afed2 = Entry(self.container2)
        self.afed2.pack(side=RIGHT)

        self.aflb3 = Label(self.container3, text="Genero", font =  fontpadrao, width=10)
        self.aflb3.pack(side=LEFT)

        lst = ["Terror", "Ação", "Comédia", "Aventura", "Esportes", "Drama", "Documentário", "Animação"]
        self.variablegen.set("Comédia")


        self.afed3 = OptionMenu(self.container3,self.variablegen,*lst)    #Entrada de genero de filme
        self.afed3['width'] = 13
        self.afed3['borderwidth'] = 2
        self.afed3.pack(side=RIGHT)

        self.aflb4 = Label(self.container4, text="Lançamento", font =  fontpadrao, width=10)
        self.aflb4.pack(side=LEFT)

        self.afed4 = Entry(self.container4)
        self.afed4.pack(side=RIGHT)


        self.afbtnok = Button(self.container5, text="Adicionar", command=  self.adicionarFilmeTop, width=10)
        self.afbtnok.pack()

    def topLevelBuscarFilme(self):  #Janela TOP-LEVEL criada(busca de filmes)
        top2 = Toplevel()
        top2.title('Buscar Filme')
        fontpadrao = ('Verdana', 8)


        #Containers
        self.bfcontainer1 = Label(top2)
        self.bfcontainer1['pady'] = 5
        self.bfcontainer1.pack()

        self.bfcontainer2 = Label(top2)
        self.bfcontainer2.pack()


        self.bfcontainer3 = Label(top2)
        self.bfcontainer3.pack()

        self.bfcontainer4 = Label(top2)
        self.bfcontainer4.pack()

        self.bfcontainer5 = Label(top2)
        self.bfcontainer5.pack()



        self.bflb0 = Label(self.bfcontainer1, text='Buscar Filme', font = ("Calibri", "13",  "bold"), width=10)
        self.bflb0.pack()

        self.bflb1 = Label(self.bfcontainer2, text='Nome', font =  fontpadrao, width = 10)
        self.bflb1.pack(side = LEFT)

        self.bfed1 = Entry(self.bfcontainer2, width=15)
        self.bfed1.pack(side = LEFT)

        self.bfbt1 = Button(self.bfcontainer2, text='Buscar')
        self.bfbt1.bind("<Button-1>", self.refresh)
        self.bfbt1.pack(side = LEFT)

        self.bflb2 = Label(self.bfcontainer4, text='Gênero', font =  fontpadrao)
        self.bflb2.pack(side = LEFT)

        lst2 = ["Todos", "Terror", "Ação", "Comédia", "Aventura", "Esportes", "Drama", "Documentário", "Animação"]
        self.variablegen2.set("Todos")
        self.bfop1 = OptionMenu(self.bfcontainer4,self.variablegen2,*lst2)
        self.bfop1['width'] = 13
        self.bfop1['borderwidth'] = 2
        self.bfop1.pack(side = RIGHT)




        self.bflbox1 = Listbox(self.bfcontainer5)
        lst3 = banco.getFilmeGenero(self.variablegen2.get())
        print(lst3)
        for item in lst3:
            self.bflbox1.insert(END, item)
        self.bflbox1.pack()

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
        fontepadrao = ("Verdana", "8")


        #Containers
        self.ccontainer1 = Frame(top3)
        self.ccontainer1['pady'] = 2
        self.ccontainer1.pack()

        self.ccontainer2 = Frame(top3)
        self.ccontainer2['padx'] = 10
        self.ccontainer2['pady'] = 2
        self.ccontainer2.pack()

        self.ccontainer3 = Frame(top3)
        self.ccontainer3['padx'] = 10
        self.ccontainer3['pady'] = 2
        self.ccontainer3.pack()

        self.ccontainer4 = Frame(top3)
        self.ccontainer4['padx'] = 10
        self.ccontainer4['pady'] = 2
        self.ccontainer4.pack()

        self.ccontainer5 = Frame(top3)
        self.ccontainer5['padx'] = 10
        self.ccontainer5['pady'] = 2
        self.ccontainer5.pack()

        self.ccontainer6 = Frame(top3)
        self.ccontainer6['padx'] = 10
        self.ccontainer6['pady'] = 2
        self.ccontainer6.pack()

        self.ccontainer7 = Frame(top3)
        self.ccontainer7['padx'] = 10
        self.ccontainer7['pady'] = 2
        self.ccontainer7.pack()

        self.ccontainer8 = Frame(top3)
        self.ccontainer8['padx'] = 10
        self.ccontainer8['pady'] = 2
        self.ccontainer8.pack()

        self.ccontainer9 = Frame(top3)
        self.ccontainer9['padx'] = 10
        self.ccontainer9['pady'] = 2
        self.ccontainer9.pack()

        self.ccontainer10 = Frame(top3)
        self.ccontainer10['padx'] = 10
        self.ccontainer10['pady'] = 2
        self.ccontainer10.pack()

        self.clb1 = Label(self.ccontainer1,text='Adicionar cliente',font = ("Calibri", "13",  "bold"))
        self.clb1.pack()

        self.clb2 = Label(self.ccontainer2, text='Nome', font =  fontepadrao, width = 10)
        self.clb2.pack(side = LEFT)

        self.ced1 = Entry(self.ccontainer2, width = 25) #Entry de nome
        self.ced1.pack(side = RIGHT)

        self.clb2 = Label(self.ccontainer3, text='Cpf', font =  fontepadrao, width = 10)
        self.clb2.pack(side = LEFT)

        self.ced2 = Entry(self.ccontainer3, width = 25) #Entry de cpf
        self.ced2.pack(side = RIGHT)

        self.clb3 = Label(self.ccontainer4, text='Telefone', font = fontepadrao, width = 10)
        self.clb3.pack(side = LEFT)

        self.ced3 = Entry(self.ccontainer4, width = 25) #Entry de telefone
        self.ced3.pack(side = RIGHT)

        self.clb4 = Label(self.ccontainer5, text='Email', font = fontepadrao, width = 10)
        self.clb4.pack(side = LEFT)

        self.ced4 = Entry(self.ccontainer5, width = 25) #Entry de email
        self.ced4.pack(side = RIGHT)

        self.clb5 = Label(self.ccontainer7, text='Endereço', font = fontepadrao, width = 10)
        self.clb5.pack(side = LEFT)

        self.ced5 = Entry(self.ccontainer7, width = 25)  # Entry de endereço
        self.ced5.pack(side = RIGHT)

        self.clb6 = Label(self.ccontainer8, text='Número', font = fontepadrao, width = 10)
        self.clb6.pack(side = LEFT)

        self.ced6 = Entry(self.ccontainer8, width = 25)  # Entry de Numero
        self.ced6.pack(side = RIGHT)

        self.clb7 = Label(self.ccontainer9, text='Bairro', font = fontepadrao, width = 10)
        self.clb7.pack(side = LEFT)

        self.ced7 = Entry(self.ccontainer9, width = 25)  # Entry de email
        self.ced7.pack(side = RIGHT)

        self.cbtn2 = Button(self.ccontainer10, text='Salvar', width=10, command=self.adicionarCliente, font = fontepadrao)
        self.cbtn2.pack()

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
            cpf = self.bced1.get()
            if (banco2.checkCpf(cpf) == False):
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
            else:
                messagebox.showinfo("Log", "Cpf não encontrado!")
        except:
            print('Erro')

    def alterarCliente(self):
        try:
            cpf = self.bced1.get()
            if(banco2.checkCpf(cpf) == False):
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
            else:
                messagebox.showinfo("Log", "Cpf não encontrado!")
        except:
            messagebox.showinfo("Log", "Erro ao alterar cliente!")

    def realizarPedidoBtn(self):
        cpf = self.bced1.get()
        if(banco2.checkCpf(cpf)==False):
            self.topRealizarPedido()
            self.cpfatual = cpf
        else:
            messagebox.showinfo("Log", "Cpf não encontrado!")



    def topLevelBuscarClientes(self):
        top4 = Toplevel()
        top4.geometry("260x260+600+100")

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
        self.bcbtn2.grid(row=9, column=0)

        self.bcbtn3= Button(top4, text='Excluir', command=self.excluirCliente)
        self.bcbtn3.grid(row=9, column=1)

        self.bcbtn4 = Button(top4, text='Pedido', command=self.realizarPedidoBtn)
        self.bcbtn4.grid(row=9, column=2)


    def realizaPedido(self):
        cpf = self.bced1.get()
        if (banco2.checkCpf(cpf) == False and self.rpsb1.get() != '0'):
            if(banco.getFilmeId(int(self.rped1.get()) != "Erro" and self.rped1.get()) != "Id não encontrado"):
                pedido = Pedidos(cpf,int(self.rped1.get()),int(self.rpsb1.get()))
                banco3.addPedido(pedido)
                messagebox.showinfo("Log", "Pedido realizado com sucesso")
            else:
                messagebox.showinfo("Log", "Informe o id correto")
        elif(self.rpsb1.get() == '0'):
            messagebox.showinfo("Log", "Coloque um número de dias")
        else:
            messagebox.showinfo("Log", "Cpf incorreto")


    def topRealizarPedido(self):
        top5 = Toplevel()
        top5.geometry("260x260+600+100")
        fontepadrao = ('Calibri',10)
        self.rplb0 = Label(top5, text='Realizar pedido', font=('Verdana',10, 'bold'))
        self.rplb0.grid(row=0,column=1)

        self.rplb1 = Label(top5, text='Id do filme', font = fontepadrao)
        self.rplb1.grid(row=1, column=0)

        self.rped1 = Entry(top5)
        self.rped1.grid(row=1,column=1)

        self.rplb2 = Label(top5, text='Dias', font=fontepadrao)
        self.rplb2.grid(row=2,column=0)

        self.rpsb1 = Spinbox(top5, from_=0, to=10)
        self.rpsb1.grid(row=2,column=1)

        self.rpbtn1 = Button(top5, text='Confirmar', command=self.realizaPedido)
        self.rpbtn1.grid(row=3, column=1)






root = Tk()
root.wm_title("Sistema Locadora")
root.geometry("800x600+250+60")
main(root)
root.mainloop()
