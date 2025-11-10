from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create (or access) the database named "todo"
db = client["todo"]

# Create (or access) a collection named "tasks"
todo_collection = db["tasks"]

print("✅ MongoDB connected and collection created successfully!")
