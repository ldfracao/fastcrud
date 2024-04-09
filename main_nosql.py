from fastapi import FastAPI
from models import Item
from control_nosql import create_item, get_all_items
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:966",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/items/")
def add_items(item: Item):
    return create_item(item)


@app.get("/items/")
def read_items():
    return get_all_items()
