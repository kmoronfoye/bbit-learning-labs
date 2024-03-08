from producer_interface import mqProducerInterface
import pika
import os


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name):
        self.name = exchange_name
        self.routing = routing_key
        self.setupRMQConnection()

    def setupRMQConnection(self):
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=self.con_params)
        self.channel = self.connection.channel()
        exchange = self.channel.exchange_declare(exchange=self.name)

    def publishOrder(self, message):

        self.channel.basic_publish(
            exchange=self.name,
            routing_key=self.routing,
            body=message,
        )
        self.channel.close()
        self.connection.close()
