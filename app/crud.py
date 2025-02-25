from bson import ObjectId
from .connection import get_db
from .models import Blog


db = get_db()
collection = db["blog"]

def get_all_blogs():
    blogs = collection.find()
    list_blog = list(blogs)

    return list_blog


def create_blog(username, title, content, tag):
    blog = Blog(username, title, content, tag)
    blog_dict = blog.to_dict()
    result = collection.insert_one(blog_dict)
    if result.inserted_id:
        return "success"
    else:
        return "fail"

def delete_blog(id):
    if collection.find_one({"_id": id}):
        collection.delete_one({"_id": id})
        return "success"
    else:
        return "fail"
    

def update_blog(id, username, title, content, tag):
    if collection.find_one({"_id": id}):
        blog = Blog(username, title, content, tag)
        new_blog = {
            "$set": blog.to_dict(id)
        }
        id = {
            "_id": id
        }
        collection.update_one({id}, {new_blog})
        return "success"
    else:
        return "fail"
    
    
def get_blog(title):
    blog = collection.find()
    if blog != None:
        list_blog = list(blog)
        list_blog_dict = []
        for i in list_blog:
            if i["title"].find(title) != -1:
                list_blog_dict.append(i)
        return list_blog_dict
    else:
        return "fail"



