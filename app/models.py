from bson import ObjectId
import hashlib
from flask_login import UserMixin

class Blog:
    def __init__(self, username, title, content, tag):
        self.username = username
        self.title = title
        self.content = content
        self.tag = tag

    def to_dict(self, id=None):
        if id == None:
            id = str(ObjectId())
        return {
            "_id": id,
            "username": self.username,
            "title": self.title,
            "content": self.content,
            "tag": self.tag
        }
    
class User(UserMixin):
    def __init__(self, username, password ,user_id=None):
        self.id = user_id or str(ObjectId())
        self.username = username
        self.password = password
    
    def to_dict(self):
        return {
            "_id": self.id,
            "username": self.username,
            "password": self.password
        }
    
    def get_id(self):  
        return str(self.id)