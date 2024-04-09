from db_nosql import create_server_connection
from models import Item
import uuid

connection = create_server_connection(
    "localhost", "root", "root123", "fastcrud")
db = connection["fastcrud"]
collection = db["items"]


def create_item(item: Item):
    item.id = str(uuid.uuid4())
    item = item.dict()
    collection.insert_one(item)
    item = str(item)
    return item


def get_all_items():
    result = []
    cursor = collection.find({})
    for document in cursor:
        result.append(document)
    return str(result)


def update_item(item_id: str, item: Item):
    item = item.dict()
    collection.update_one(
        {'id': item_id},
        {'$set': {
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'on_offer': item.on_offer
        }
        }
    )
    return item


def delete_item(item_id: str):
    collection.delete_one({"id": item_id})
    return {"message": "item deleted successfully"}
