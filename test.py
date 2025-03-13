import secrets
import os
import hashlib

# สร้าง Secret Key ความยาว 32 bytes
secret_key = secrets.token_hex(32)  # ใช้ 32 bytes (64 ตัวอักษรในรูปแบบ hex)



password = "1234"
password = hashlib.sha256(password.encode('utf-8')).hexdigest()
print(password)