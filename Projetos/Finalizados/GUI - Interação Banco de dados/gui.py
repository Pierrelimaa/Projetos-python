
from tkinter import *
from db import DB

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container_1 = Frame(master)
        self.container_1["pady"] = 10
        self.container_1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container_2 = Frame(master)
        self.container_2["padx"] = 20
        self.container_2["pady"] = 5
        self.container_2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container_3 = Frame(master)
        self.container_3["pady"] = 10
        self.container_3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 15
        self.container10.pack()

        # self.titulo = Label(self.container1, text="Informe os dados :")
        # self.titulo["font"] = ("Calibri", "15", "bold")
        # self.titulo.pack(side = TOP)

        self.titulo2 = Label(self.container_1, text="ATUALIZAÇÃO DE DADOS")
        self.titulo2["font"] = ("Calibri", "11")
        self.titulo2.pack(side=LEFT)

        self.lblidusuario = Label(self.container2,
        text="ID:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.lbletapa = Label(self.container2,
        text="Etapa:", font=self.fonte, width=10)
        self.lbletapa.pack(side=LEFT)

        self.txtetapa = Entry(self.container2)
        self.txtetapa["width"] = 10
        self.txtetapa["font"] = self.fonte
        self.txtetapa.pack(side=LEFT)


        self.titulo3 = Label(self.container_3, text="INSERIR NOVO PEDIDO")
        self.titulo3["font"] = ("Calibri", "11")
        self.titulo3.pack(side=LEFT)
      

        self.lblnome = Label(self.container4, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblfrase = Label(self.container5, text="Frase:",
        font=self.fonte, width=10)
        self.lblfrase.pack(side=LEFT)

        self.txtfrase = Entry(self.container5)
        self.txtfrase["width"] = 25
        self.txtfrase["font"] = self.fonte
        self.txtfrase.pack(side=LEFT)

    

        self.lblempresa = Label(self.container6, text="Empresa:",
        font=self.fonte, width=10)
        self.lblempresa.pack(side=LEFT)

        self.txtempresa = Entry(self.container6)
        self.txtempresa["width"] = 25
        self.txtempresa["font"] = self.fonte
        self.txtempresa.pack(side=LEFT)


        self.lblemail= Label(self.container7, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container7)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)
        
        self.lblproduto= Label(self.container8, text="Produto:",
        font=self.fonte, width=10)
        self.lblproduto.pack(side=LEFT)

        self.txtproduto = Entry(self.container8)
        self.txtproduto["width"] = 25
        self.txtproduto["font"] = self.fonte
        self.txtproduto.pack(side=LEFT)

        self.bntInsert = Button(self.container9, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container2, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (padx=15 ,side=LEFT)


        self.lblmsg = Label(self.container10, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack() 

# Criação do checklist

 

        self.lng = Checkbar(self.container_2, ['(<)', '(=)', '(>)'])
        self.lng.pack(side=TOP,  fill=X)
        self.lng.config(bd=2)

    def inserirUsuario(self):
        nome = self.txtnome.get()
        frase = self.txtfrase.get()
        empresa = self.txtempresa.get()
        email = self.txtemail.get()
        produto = self.txtproduto.get()
        
        dados = {'Nome': nome, 'Frase': frase, 'Empresa': empresa, 'Mail': email, 'Produto': produto}
        
        DB(data = dados, op= 'in')

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtempresa.delete(0, END)
        self.txtproduto.delete(0, END)


    def alterarUsuario(self):
        # user = Usuario
        etapa = self.txtetapa.get()
        id = self.txtidusuario.get()
        condicao = []
                
        for i in range(len(self.lng.vars)):
            condicao.append(self.lng.vars[i].get())
        print(condicao)

        # Atualiza os valores no banco de dados
        DB(data = {'id': id, 'condicao': condicao ,"etapa": etapa}, op= 'up')

        # Deleta os dados de atualização
        self.txtidusuario.delete(0, END)
        self.txtetapa.delete(0, END)
    
    def excluirUsuario(self):
        # 
        pass



class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)



if __name__ == '__main__':
    root = Tk()
    Application(root)
    root.mainloop()