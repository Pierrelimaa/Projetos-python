import paho.mqtt.client as paho
import time
import pyodbc 

broker = "weblab.maua.br"
port = 1883

class Update:
    def __init__(self, client):
        self.user = ''
        self.password = ''
        self.server = ''
        self.database =  ''
        self.client = client

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.user + ';PWD=' + self.password) 
        self.cursor = conn.cursor()

        self.etapas = ['fila', 'metrologia', 'proxpersonalizacao', 'puncionamento', 'laser']
        self.pub(self.client)


    def on_publish(self):   # create function for callback
        print("data published \n")


    def select_db(self, etapa):
        counter = 0
        self.cursor.execute('SELECT TOP 1 id, nome, frase FROM [blocoA].[dbo].[Pedido] WHERE etapa =' + str(etapa))
        counter += 1

        for row in self.cursor: 
            counter -= 1

        if counter == 1:
            row = ('-', '-', '-')
    
        return row


    def pub(self, client1):
        print('------')
        aux = []

        for t in range(1, 6, 1):
            aux.append(self.select_db(t))

        print(aux)

        for i in range(5):
            ret = client1.publish("maua40/fabricando/" + self.etapas[i],'{"Nome":"' + str(aux[i][1]) + '","Frase":"' + str(aux[i][2]) + '", "ID":"' + str(aux[i][0]) + '"}')
            
            time.sleep(0.5)

