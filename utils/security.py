import hashlib
import json
import os
from config.config import USERS_FILE, MAX_LOGIN_ATTEMPTS, normalize_username, get_default_user


class SecurityManager:
    """Foydalanuvchilarni xavfsiz boshqarish uchun yordamchi klass."""

    @staticmethod
    def hash_password(password):
        """Parolni SHA-256 bilan hash qiladi."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password, hash_password):
        """Kiritilgan parol va saqlangan hashni solishtiradi."""
        return SecurityManager.hash_password(password) == hash_password

    @staticmethod
    def load_users():
        """Foydalanuvchilarni users.json fayldan o'qiydi."""
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    @staticmethod
    def save_users(users):
        """Foydalanuvchilarni users.json faylga yozadi."""
        directory = os.path.dirname(USERS_FILE)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(USERS_FILE, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=2, ensure_ascii=False)

    @staticmethod
    def find_user(username):
        """Foydalanuvchining ma'lumotini qaytaradi."""
        normalized = normalize_username(username)
        users = SecurityManager.load_users()
        for user in users:
            if normalize_username(user.get("username", "")) == normalized:
                return user
        return None

    @staticmethod
    def add_user(username, password):
        """Yangi foydalanuvchini qo'shadi."""
        existing = SecurityManager.find_user(username)
        if existing:
            return False

        users = SecurityManager.load_users()
        users.append({
            "username": username,
            "password": SecurityManager.hash_password(password)
        })
        SecurityManager.save_users(users)
        return True

    @staticmethod
    def authenticate(username, password):
        """Foydalanuvchini login qiladi."""
        user = SecurityManager.find_user(username)
        if not user:
            return False

        return SecurityManager.verify_password(password, user.get("password", ""))

    @staticmethod
    def ensure_default_user():
        """Agar users.json bo'sh bo'lsa, default foydalanuvchini yaratadi."""
        users = SecurityManager.load_users()
        if users:
            return

        default = get_default_user()
        SecurityManager.add_user(default["username"], default["password"])

    @staticmethod
    def login_attempts_remaining(attempts):
        """Qolgan urinishlar sonini hisoblaydi."""
        return MAX_LOGIN_ATTEMPTS - attempts
