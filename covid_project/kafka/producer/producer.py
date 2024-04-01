import time
import json
from confluent_kafka import Producer
import requests

BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'covid_data'

url = 'https://disease.sh/v3/covid-19/countries'

try:
    producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for country_data in data:
                country_name = country_data['country']
                
                key = country_name.encode('utf-8')
                value = json.dumps(country_data).encode('utf-8')
                producer.produce(KAFKA_TOPIC, key=key, value=value)
                producer.flush()
                print("Successfully sent a message to Kafka.")

        else:
            print(f"Error: {response.status_code} - {response.text}")

        time.sleep(10)

except KeyboardInterrupt:
    print("Program terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")
