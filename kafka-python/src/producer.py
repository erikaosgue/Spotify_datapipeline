""" 
Kafka Producer 
"""
import json
from datetime import datetime
from kafka import KafkaProducer


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=serializer
)

# producer function get's call in the get_playlist_from_spotify.py
def producer_func(message):
        print(f'Producing message @ {datetime.now()} | Message = {str(message)}')
        producer.send('messages', message)

