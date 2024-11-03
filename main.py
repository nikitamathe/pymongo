from pymongo import MongoClient
client = MongoClient(host='localhost', port=27017, document_class=dict, tz_aware=False, connect=True, **kwargs)
db = client.test_database

posts = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14),
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45),
    },
]
result = posts.insert_many(new_posts)
result.inserted_ids
[ObjectId('...'), ObjectId('...')]

db.