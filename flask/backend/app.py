import os

from flask import Flask, jsonify, request
from flask.cli import load_dotenv
import pymongo


load_dotenv()

mongo_uri = os.getenv("mongo_uri")

client = pymongo.MongoClient(mongo_uri)

db = client["learning"]

collection = db["sample_data"]

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def submit_data():
    data = request.get_json()
    print("received",data)
    collection.insert_one(data)
    return jsonify({"message": "Data submitted successfully"}), 201

@app.route('/view', methods=['GET'])
def view_data():
    data = list(collection.find())
    for item in data:
        print(item)
        del item["_id"]  # Remove the ObjectId field for JSON serialization
    return jsonify(data), 200

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    print("received", data)
    collection.insert_one(data)
    return jsonify({"message": "Todo item submitted successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
