from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
db = client["fraud_detection_db"]
transactions = db["transactions"]

fraud_count = transactions.count_documents({"fraud": True})
safe_count = transactions.count_documents({"fraud": False})

plt.bar(["Fraud", "Safe"], [fraud_count, safe_count])
plt.title("Fraud Detection Report")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()