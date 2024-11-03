import pymongo # pymongo is a tool to connect mogodb with python
from pymongo import MongoClient # from pymongo we imported mongoclient,to manage the connection to a MongoDB instance and interact with its databases and collections
client = MongoClient("mongodb://localhost:27017/") # we connected mongoclient using url 
db = client["test-database"] #created a database
collection = db["test-collection"] # created a collection
collection.insert_one({"name":"John", "email": "john@gmail.com", "age": 30}) # inserted data first to create database 
print(collection) 