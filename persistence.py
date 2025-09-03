import firebase_admin
from firebase_admin import credentials, firestore

class FireStoreDB:
    _instance = None
    def __new__(cls, key_path=None): # instância da classe (Singleton)
        if cls._instance is None:
            cls._instance = super(FireStoreDB, cls).__new__(cls)
            firebase_admin.initialize_app(credentials.Certificate(key_path))
            cls._instance.db = firestore.client()
        return cls._instance
    
    def get_collection(self, collection, raw = False): # retorna todos os documentos da collection ou a collection em si (CollectionReference)
        docs = self.db.collection(collection) if collection.__class__.__name__ == "str" else collection
        if raw:
            return docs
        response = []
        for doc in docs.get():
            response.append(doc.to_dict())   
        return response
    
    def insert_into_collection(self, collection, document: dict): # insere um documento em uma determinada collection
        try:
            target = self.db.collection(collection) if collection.__class__.__name__ == "str" else collection
            target.add(document)
        except:
            return False
        finally:
            return True
        
    def get_document_by_value(self, collection, field: str, value, raw = False): # retorna documento(s) a partir de um valor de determinado campo; em dict ou em DocumentSnapshot
        target = self.db.collection(collection) if collection.__class__.__name__ == "str" else collection
        if raw:
            return target.where(field, "==", value).get()
        response = []
        for doc in target.where(field, "==", value).get():
            response.append(doc.to_dict())
        return response
    
    def get_document_by_id(self, collection, document_id, raw = False):
        target = (self.db.collection(collection) if collection.__class__.__name__ == "str" else collection).document(document_id)
        if raw:
            return target
        return target.get().to_dict()    

        
    
    


        
