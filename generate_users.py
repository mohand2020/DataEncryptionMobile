import hashlib
from cryptography.fernet import Fernet
import json

# بيانات المستخدمين
users = [
    {"username": "user1@safe", "password": "pass1234!"},
    {"username": "user2@secure", "password": "myKey@2025"}
]

# توليد الملف
data = {"users": []}
for u in users:
    password_hash = hashlib.sha256(u["password"].encode()).hexdigest()
    encryption_key = Fernet.generate_key().decode()
    data["users"].append({
        "username": u["username"],
        "password_hash": password_hash,
        "encryption_key": encryption_key
    })

# حفظ الملف
with open("users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("✅ users.json generated successfully.")
