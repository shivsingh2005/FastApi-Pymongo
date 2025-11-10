# 🚀 FastAPI + MongoDB (PyMongo) Example

This project demonstrates how to **connect FastAPI with MongoDB** using **PyMongo**, perform CRUD operations, and run the API locally.

---

## 🧠 Overview

This repository provides a simple, beginner-friendly example showing how to integrate **FastAPI** with **MongoDB** using **PyMongo** — without using any ORM like Motor or Beanie.  
It’s perfect for learning how REST APIs interact with MongoDB in real-time.

---

## 🧩 Tech Stack

- **FastAPI** — Backend framework  
- **MongoDB** — NoSQL database  
- **PyMongo** — MongoDB driver for Python  
- **Uvicorn** — ASGI server for running FastAPI apps  

---

## ⚙️ Project Structure

FAstApi-Pymongo/
│
├── main.py # Entry point (FastAPI app)
├── database.py # MongoDB connection setup
├── model.py # Schema/model structure (if defined)
├── routes/
│ └── todo.py # CRUD routes for Todo app
├── serializers/
│ └── todo_serializers.py # Serializers to convert MongoDB docs
├── requirements.txt # Dependencies
└── README.md # This file



---

## 🧰 Setup Instructions (Run Locally)

Follow these simple steps to run the project on your local system 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shivsingh2005/FastApi-Pymongo.git
cd FastApi-Pymongo


2️⃣ Create a Virtual Environment
python -m venv mongoenv

3️⃣ Activate the Environment
mongoenv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Start MongoDB
You can modify the URI in your database.py:
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["todo"]

▶️ Run the FastAPI App
uvicorn main:app --reload

⭐ Contribute

Feel free to fork this repo and improve it.
Pull requests are always welcome! 🚀
