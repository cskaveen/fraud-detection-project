'''from pymongo import MongoClient
from fraud_rules import check_fraud
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection_db"]
transactions = db["transactions"]

# Simulated live transaction
new_transaction = {
    "transaction_id": 2,
    "user_id": "U002",
    "amount": 25000,
    "location": "Mumbai",
    "transactions_last_min": 4,
    "timestamp": str(datetime.now())
}

# Check fraud
fraud_reasons = check_fraud(new_transaction)

if fraud_reasons:
    new_transaction["fraud"] = True
    new_transaction["reasons"] = fraud_reasons
    print("⚠ FRAUD DETECTED")
    print("Reason:", fraud_reasons)
else:
    new_transaction["fraud"] = False
    print("✅ SAFE TRANSACTION")

# Save to MongoDB
transactions.insert_one(new_transaction)

print("✅ Transaction saved to MongoDB")
'''
from pymongo import MongoClient
from fraud_rules import check_fraud
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection_db"]
transactions = db["transactions"]

while True:
    print("\n--- New Transaction ---")
    
    transaction_id = int(input("Enter transaction ID: "))
    user_id = input("Enter user ID: ")
    amount = float(input("Enter amount: "))
    location = input("Enter location: ")
    count = int(input("Transactions in last minute: "))

    new_transaction = {
        "transaction_id": transaction_id,
        "user_id": user_id,
        "amount": amount,
        "location": location,
        "transactions_last_min": count,
        "timestamp": str(datetime.now())
    }

    fraud_reasons = check_fraud(new_transaction)

    if fraud_reasons:
        new_transaction["fraud"] = True
        new_transaction["reasons"] = fraud_reasons
        print("⚠ FRAUD DETECTED:", fraud_reasons)
    else:
        new_transaction["fraud"] = False
        print("✅ SAFE TRANSACTION")

    transactions.insert_one(new_transaction)
    print("Saved to MongoDB")

    choice = input("Check another transaction? (y/n): ")
    if choice.lower() != "y":
        break