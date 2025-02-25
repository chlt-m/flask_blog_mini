from .models import User
from .connection import get_db
import hashlib

db = get_db()
collection = db["user"]

def user_get(username):
    user = collection.find_one({"username": username})
    if user:
        return User(user["username"], user["password"], user["_id"])
    else:
        return None

def user_add_api(username, password):
    user = User(username, password)
    user_dict = user.to_dict()
    if user_get(username):
        return "Username already exists"
    else:
        collection.insert_one(user_dict)
        return "success"

def user_login_validate(username, password):
    user = user_get(username)
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if user and user.password == password:
        return "success"
    else:
        return "fail"
    

def password_hash(password):
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password



