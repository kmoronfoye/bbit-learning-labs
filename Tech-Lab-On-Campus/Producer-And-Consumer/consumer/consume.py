#!/usr/bin/env python

# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pika
import os
import sys
from consumer_sol import mqConsumer# pylint: disable=import-error

# import mqconsu

def main() -> None:
    consumer = mqConsumer(binding_key="Tech Lab Key",exchange_name="Tech Lab Exchange",queue_name="Tech Lab Queue")
    consumer.startConsuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# class mqConsumer(mqConsumerInterface):
#      def __init__(self, binding_key: str, exchange_name: str, queue_name: str):
#          self.routing = binding_key
#          self.exchange = exchange_name
#          self.queue = queue_name
#          self.setupRMQConnection()
         
# def setupRMQConnection(self):
#     self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
#     self.connection = pika.BlockingConnection(parameters=self.con_params)
#     self.channel.queue_declare(queue="queue")
#     self.channel.queue_bind(queue= "queue",routing_key= "Routing Key",exchange="exchange",)
#     self.channel.basic_consume("queue", on_message_callback, auto_ack=False)

# def on_message_callback(self, channel, method_frame, header_frame, body):
#     print()
#     self.channel.basic_ack(method_frame.delivery_tag, False)
      
      

# def startConsuming(self):
#     print(" [*] Waiting for messages. To exit press CTRL+C")
#     self.channel.start_consuming()
    
      



# def __del__(self): 
#     print('Closing RMQ connection on destruction')
#     self.channel.close()
#     self.connection.close()
    
    