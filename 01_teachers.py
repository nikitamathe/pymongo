import pymongo
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client["Teachers"]
collection = db["Teachers_Data"]
collection.insert_many([{"Name":"John","Email":"john@gmail.com","Designation":"HOD","Address":"Pune","Age":30,"Contact":1111111111},{"Name":"Jack","Email":"jack@gmail.com","Designation":"Professor","Address":"Pune","Age":50,"Contact":2222222222},{"Name":"Andrew","Email":"Andrew@gmail.com","Designation":"Professor","Address":"Mumbai","Age":40,"Contact":3333333333}])
