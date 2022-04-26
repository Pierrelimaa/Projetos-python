from queue import PriorityQueue
import paho.mqtt.client as mqtt
import json
from db import DB



class Client(DB):
# class Client():
    def __init__(self): # Array contendo as chaves do dicionario que vai atualizar o DB

        self.client_id = 'Mosquitto weblab'
        self.clean_session = True
        self.userdata = None
        self.protocol = mqtt.MQTTv311
        self.transport = 'tcp'

        self.username = '*****'
        self.password = '****'

        self.host = 'weblab.maua.br'
        self.port = 1883


    def on_connect(self, client, userdata, flags, rc):  # The callback for when the client connects to the broker
        if rc == 0 :
            print("Connection success. Code: {0}".format(str(rc)))  # Print result of connection attempt
        
            client.subscribe("maua40/pedidos/in")  # Subscribe to the topic “digitest/test1”, receive any messages published on it
            client.subscribe("maua40/pedidos/out")
        else:
            print("Failed. Code: {}".format(str(rc)))


    def on_message(self, client, userdata, msg):    # The callback for when a PUBLISH message is received from the server
        print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
        dados = str(msg.payload)
   
        parsed_msg = json.loads(msg.payload.decode())
        print(parsed_msg)
        if 'out' in msg.topic :
            self.retirada(data = parsed_msg)

        else :
            self.get_data(msg = parsed_msg)
            

    def on_publish(self, client, userdata, result): # create function for callback
        print("data published \n")


    def get_data(self, msg): # entrada de pedidos

        if msg['Produto'] == True:
            msg['Produto'] = 1
        else:
            msg['Produto'] = 0

        for key in msg:
            print( key,':' , msg[str(key)])

        var = DB(data = msg, op = 'e') 
        msg = client.publish("maua40/pedidos/confirm", var.select_db())

    

    def retirada(self, data):

        pedido = data['ID']

        print(pedido)
        var = DB(data = pedido, op = 'r')
        msg = client.publish("maua40/pedidos/outconfirm", var.update_db(int(pedido)))


teste = Client()

client = mqtt.Client(teste.client_id, teste.clean_session, teste.userdata, teste.protocol, teste.transport)

client.on_connect = teste.on_connect  # Define callback function for successful connection
client.on_message = teste.on_message  # Define callback function for receipt of a message
client.on_publish = teste.on_publish 

client.username_pw_set(teste.username, teste.password)
client.connect(teste.host, teste.port)


while True:
    client.loop()
    # Update(client = client)




