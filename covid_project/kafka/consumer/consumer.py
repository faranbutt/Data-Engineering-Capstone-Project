from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Consumer, KafkaError
import json
from google.cloud import storage
import pandas as pd
import os
import time

key_path = os.path.join('/faran/user/zoomcamp/kafka_project', 'key.json')

BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'covid_data'
GROUP_ID = 'my_consumer_group'
GCS_BUCKET_NAME = 'data_tlk_388'
GCS_FILE_NAME = 'covid_data.csv'  

consumer_conf = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(consumer_conf)

admin_client_conf = {'bootstrap.servers': BOOTSTRAP_SERVERS}
admin_client = AdminClient(admin_client_conf)

existing_topics = admin_client.list_topics().topics
if KAFKA_TOPIC not in existing_topics:
    new_topic = NewTopic(KAFKA_TOPIC, num_partitions=1, replication_factor=1)
    admin_client.create_topics([new_topic])

consumer.subscribe([KAFKA_TOPIC])

gcs_client = storage.Client.from_service_account_json(key_path)

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        try:
            covid_data = json.loads(msg.value().decode('utf-8'))
            print(f"Received COVID-19 data: {covid_data}")

            covid_df = pd.DataFrame([covid_data])


            bucket = gcs_client.get_bucket(GCS_BUCKET_NAME)
            blob = bucket.blob(GCS_FILE_NAME)

            existing_content = blob.download_as_string() if blob.exists() else ""

            if isinstance(existing_content, bytes):
                existing_content = existing_content.decode('utf-8')

            new_content = existing_content + covid_df.to_csv(index=False, header=not blob.exists())

            blob.upload_from_string(new_content, content_type='text/csv')

            time.sleep(2) 

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

except KeyboardInterrupt:
    print("Consumer terminated by user.")
finally:
    
    consumer.close()
