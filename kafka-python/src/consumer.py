"""
Kafka Consumer 
"""

import json 
from kafka import KafkaConsumer
import signal
import sys


def signal_handler(sig, frame):
    """ 
    Handler for catching the CRL + C keywords
    """
    print('\n= BYE! =')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
     
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='kafka:9092',
        # Running the consumer in the localhost
        # bootstrap_servers='localhost:9092',

        auto_offset_reset='earliest'
    )
    for message in consumer:
        print("message: ", message.value)
        print(json.loads(message.value))


