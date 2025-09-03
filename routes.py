from main import app, database
from flask import jsonify, request


@app.route("/") # teste
def hello_world():
    return "Hello World"

@app.route("/collection", methods=["POST"]) # teste
def get_collection():
    return jsonify(database.get_collection(request.form.get("collection")))

@app.route("/collection/add", methods=["POST"]) # teste
def add_to_collection():
    collection,document = request.get_json().values()
    return "Added" if database.insert_into_collection(collection, document) else "Failed to add"

@app.route("/collection/document", methods=["POST"]) # teste
def get_document_by_value():
    collection,field,value = request.get_json().values()
    return jsonify(database.get_document_by_value(collection, field, value))

@app.route("/collection/document/id", methods=["POST"]) # teste
def get_document_by_id():
    collection,document_id = request.get_json().values()
    return jsonify(database.get_document_by_id(collection, document_id))