from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def create_server_connection(host_name, user_name, password, db_name):
    client = None
    try:
        client = MongoClient(host=host_name,
                             username=user_name,
                             password=password,
                             authSource=db_name,
                             authMechanism='SCRAM-SHA-256')
        print("MongoDB connection successfull")
    except ConnectionFailure as err:
        print(f"Error: '{err}'")

    return client
