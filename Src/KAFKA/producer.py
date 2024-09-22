import requests
import os
import sys
import json
import yaml
from kafka import KafkaProducer
import time
from Components.get_config_file import get_config_Full_file


def fetch_data_from_api(API_URL):
    try:
        response = requests.get(API_URL)
        print(response)
        if response.status_code == 200:
            return response.json().get('results',[])
        return []

    except Exception as e:
       pass


def Send_message_to_cluster(producer,kafka_topic, API_URL):
    try:
        print("1: The Cluster Topic is ",kafka_topic)
        while True:
            data = fetch_data_from_api(API_URL)
            if data:
                for item in data:
                    record = {
                        'first': item['name']['first'],
                        'last': item['name']['last'],
                        'email': item['email'],
                        'phone': item['phone'],
                        'dob': item['dob']['date']
                    }
                    producer.send(kafka_topic, value = record)
            time.sleep(3)

    except Exception as e:
        pass


if __name__ == "__main__":
     full_config_file = get_config_Full_file()
     API_URL = full_config_file['Main_API']
     KafKa_Topic = full_config_file['Kafka_Topic_Name']
    
     producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
     Send_message_to_cluster(producer, KafKa_Topic, API_URL)

        
  
    