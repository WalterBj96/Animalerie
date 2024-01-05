from flask import *
from pymongo import MongoClient
from routes import init_routes

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["animalerie"]
animal_collection = db ['animal']
stock_collection = db ['stock']
transaction_collection = db ['transaction']

init_routes(app,animal_collection, stock_collection, transaction_collection)

if __name__== '__main__':
    app.run(debug=True)