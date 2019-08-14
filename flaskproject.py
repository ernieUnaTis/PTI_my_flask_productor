from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")

def greeting():
	return "<h1 style='color:green'>Hello World!</h1>"


@app.route("/productor", methods=['GET', 'POST'])
def publish():
	import pika

	#Leer XML POST
	import xmltodict
	xmlPost = request.data

	#Publicar en RabbitMQ
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='notificacion_terceros')
	channel.basic_publish(exchange='',
                      routing_key='notificacion_terceros',
                      body=xmlPost)
	print(" [x] Evento Encolado")
	connection.close()
	return 'OK'

if __name__ == "__main__":
	app.run(host='0.0.0.0')
