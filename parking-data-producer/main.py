import time
import orjson as orjson
from faker import Faker
from kafka import KafkaProducer
import numpy as np

fake = Faker()


def get_parking_data():
    return {
        'username': fake.user_name(),
        'ip_address': fake.ipv4()
    }


# function to create a dataframe with fake values for parking
def parking_data():
    # lists to randomly assign to Parking info
    parking_status_list = ['Ongoing', 'exit']
    car_type_list = ['Electric', 'Conventional']
    parking_location_list = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

    fake_data = [{'parking_id': fake.isbn10(),
                  'userName': fake.user_name(),
                  'parking_date': fake.date_time_between(start_date='-140m', end_date='now'),
                  'parking_duration': np.random.randint(120),
                  'Parking_Location': np.random.choice(parking_location_list, p=[0.30, 0.25, 0.15, 0.15, 0.10, .05]),
                  'Worker Status': np.random.choice(parking_status_list, p=[0.30, 0.70]),
                  # assign items from list with different probabilities
                  'car_type': np.random.choice(car_type_list, p=[0.30, 0.70]),

                  }]
    while 1 == 1:
        return fake_data


def json_serializer(data):
    return orjson.dumps(data)


producer = KafkaProducer(bootstrap_servers='localhost:29092',
                         client_id="python_producer",
                         value_serializer=json_serializer,
                         acks='all'
                         )

if __name__ == "__main__":
    i = 0
    while 1 == 1:
        parkingdata = parking_data()
        print("Parking data is: ", parkingdata)
        producer.send(topic='test_topic', value=parkingdata).get()
        # print("Message is: ", msg)
        producer.flush()
        time.sleep(1)
