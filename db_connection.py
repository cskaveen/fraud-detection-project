from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection_db"]
transactions = db["transactions"]

sample_data = {
    "transaction_id": 1,
    "user_id": "U001",
    "amount": 5000,
    "location": "Chennai",
    "fraud": False
}

transactions.insert_one(sample_data)

print("✅ Data inserted successfully")