from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['blog_demo']

def get_db():
    return db