import yaml
import csv
import os
from kafka import KafkaConsumer
import json
from Components.get_config_file import get_config_Full_file


def write_to_csv(data, Consumer_data_store_location):
    if not os.path.exists(Consumer_data_store_location):
        os.makedirs(Consumer_data_store_location)

    file_path = os.path.join(Consumer_data_store_location, 'api_data.csv')
    fileLocationexists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        if not fileLocationexists:
            writer.writerow(['first', 'last', 'email', 'phone', 'dob'])
        writer.writerow([
            data.get('first', ''),
            data.get('last', ''),
            data.get('email', ''),
            data.get('phone', ''),
            data.get('dob', ''),
        ])

def consumer_data_store(consumer, Consumer_data_store_location):
    try:
        for message in consumer:
            consumer_data = message.value.decode('utf-8')  # Corrected typo here
            if consumer_data:
                data = json.loads(consumer_data)

                if isinstance(data, dict):
                    write_to_csv(data, Consumer_data_store_location)
                else:
                    print("Data not received, expected a dictionary.")
    except Exception as e:
        print(f"An error occurred: {e}")  # Logging errors

def run_consumer():
    full_config_file = get_config_Full_file()
    Consumer_data_store_location = full_config_file['StoreApiDataIn']
    KafKa_Topic = full_config_file['Kafka_Topic_Name']

    consumer = KafkaConsumer(
        KafKa_Topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='api_group'
    )

    consumer_data_store(consumer, Consumer_data_store_location)
