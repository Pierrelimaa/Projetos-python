# # import mysql.connector

# # MySQL
# # class DB:
# #     def __init__(self,data):
# #         self.host = "localhost"
# #         self.user = "root"
# #         self.password = "****"
# #         self.database =  "****"
# #         self.data = data

# #         self.insert_db(self.data)

# #     def insert_db(self,data):    
# #         mydb = mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database )
# #         mycursor = mydb.cursor()
# #         sql = "INSERT INTO dados2 (Nome,Empresa,Frase,Mail,Produto) VALUES (%s, %s, %s, %s, %s )"
# #         val = (data["Nome"], data["Empresa"], data["Frase"], data["Mail"], data["Produto"])
# #         # val = ("TESTE","MAUS", "MAUAS", "MASD@GMAIL.COM",1)
# #         mycursor.execute(sql, val)

# #         mydb.commit()

# #         print(mycursor.rowcount, "record inserted.")

# # if __name__ == "__main__":
# #     db = DB()    


# #  TESTES MSSQL
#     # user: '',
#     # password: '',
#     # server: '',
#     # database: ''


# # Banco de dados MSSQL
from datetime import datetime
import pyodbc 

import paho.mqtt.client as mqtt

# # # Classe DB é definida como classe pai
# # class DB(object):
class DB:
    def __init__(self, data, op):
        self.user = ''
        self.password = ''
        self.server = ''
        self.database =  ''
        self.data = data

        
        if op == "r":
            var  = int(self.data)
            # self.update_db(var)
        else:
            self.insert_db(self.data)
        # self.select_db()

    def connect_db(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+ self.database+';UID='+ self.user+';PWD='+ self.password) 
        # self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+ self.database+';UID='+ self.user+';PWD='+ self.password) 
        self.cursor = self.conn.cursor()

    def insert_db(self,data): # Entrada de pedido


        self.connect_db()
        sql = """INSERT INTO [blocoA].[dbo].[Pedido] (nome,frase,empresa,email,tipoPeca,dt_entrada,etapa) VALUES (?,?,?,?,?,?, ?)"""
        # val = (data["Nome"], data["Empresa"], data["Frase"], data["Mail"], data["Produto"])
        horario = datetime.today()
        self.cursor.execute(sql, data["Nome"], data["Frase"],data["Empresa"], data["Mail"], data["Produto"], horario, 0)
        self.conn.commit()

        # for row in self.conn.commit:
        #     print(row)r

        print(self.cursor.rowcount, "record inserted.")
        # self.select_db()


    def update_db(self, data):# Para retirada

        self.connect_db()
        id = data
        sql = """UPDATE [blocoA].[dbo].[Pedido] SET etapa = 7 WHERE id = ? AND etapa = 6"""
        # print(id)
        # print(type(id))
        self.cursor.execute(sql,id)
        self.conn.commit()

        print(self.cursor.rowcount, "rows updated.")
        if self.cursor.rowcount == 0:
            # client = mqtt.Client(client_id="Mosquitto weblab",clean_session=True,userdata=None,protocol=mqtt.MQTTv311,transport="tcp") 
            # client.username_pw_set(username="PUBLIC",password="public")
            # client.connect('weblab.maua.br', 1883)
            
            # msg= client.publish("maua40/pedidos/outconfirm",'"false"')
            return '"false"'
                    
        else:
        #     client = mqtt.Client(client_id="Mosquitto weblab",clean_session=True,userdata=None,protocol=mqtt.MQTTv311,transport="tcp") 
        #     client.username_pw_set(username="PUBLIC",password="public")
        #     client.connect('weblab.maua.br', 1883)

        #    # msg= client.publish("maua40/pedidos/outconfirm","true") 
        #     msg= client.publish("maua40/pedidos/outconfirm",'"true"')
            return '"true"'



    resp = 'teste'
    def select_db(self):# Devolver o id do pedido 
        self.connect_db()

        self.cursor.execute('SELECT TOP 1 id FROM [blocoA].[dbo].[Pedido] ORDER BY id DESC')

        for row in self.cursor:
            id = row
            resp = "Seu pedido foi recebido com sucesso. ID: " + str(id[0])
            print("Seu pedido foi recebido com sucesso. ID: {}".format(id[0]))
            print(id[0])
            
        return id[0]


        
        # client = mqtt.Client(client_id="testehenrique",clean_session=True,userdata=None,protocol=mqtt.MQTTv311,transport="tcp")
        # client = mqtt.Client(client_id="Mosquitto weblab",clean_session=True,userdata=None,protocol=mqtt.MQTTv311,transport="tcp") 
        
        # # ----
        # client.username_pw_set(username="PUBLIC",password="public")
        # client.connect('weblab.maua.br', 1883)
        # # msg= client.publish("id_pedido",resp)

        # msg= client.publish("maua40/pedidos/confirm",id[0])
        

# # Testes
# # las = {"nome":"sd"}
# # l = {"Nome":"Pedro", "Empresa":"LAS", "Frase":"AMS", "Mail":"cleitin484@gmail.com", "Produto":1,}
# # if __name__ == "__main__":
# #     # db = DB(l,'a')
# #     db = DB() 


# # -maua40/pedidos/outconfirm
# # DB envia confirmação de que o pedido será retirado ou não está pronto.
# # Exemplo: "true" - Avisa que o pedido será retirado
# #                 "false" - Avisa que a peça ainda não está pronta


