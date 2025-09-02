import firebase_admin
from firebase_admin import credentials

class FireStoreDB:
    _instance = None
    def __new__(cls, key_path=None):
        if cls._instance is None:
            cls._instance = super(FireStoreDB, cls).__new__(cls)
            firebase_admin.initialize_app(credentials.Certificate(key_path))
        return cls._instance
