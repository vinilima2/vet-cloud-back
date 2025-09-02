from flask import Flask
import os
from dotenv import load_dotenv
from persistence import FireStoreDB

load_dotenv("firebase_key.env")

app = Flask(__name__)
database = FireStoreDB(os.getenv("FIREBASE_KEY"))

from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 