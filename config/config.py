import os
from datetime import datetime


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES = [
    "Oziq-ovqat",
    "Transport",
    "Kiyim",
    "Ko'ngilochar",
    "Boshqa"
]

JSON_FILE = os.path.join(ROOT_DIR, "expenses.json")
USERS_FILE = os.path.join(ROOT_DIR, "users.json")
MAX_LOGIN_ATTEMPTS = 3
DEFAULT_CURRENCY = "so'm"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_file_path(filename):
    return os.path.join(ROOT_DIR, filename)


def format_amount(amount):
    return f"{int(amount)} {DEFAULT_CURRENCY}"


def format_datetime(value=None):
    if value is None:
        value = datetime.now()

    if isinstance(value, str):
        return value

    return value.strftime(DATE_FORMAT)


def validate_category(category):
    return category in CATEGORIES


def category_menu_lines():
    return [f"{index}. {name}" for index, name in enumerate(CATEGORIES, start=1)]


def category_menu_text():
    return "\n".join(category_menu_lines())


def ensure_path_exists(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def normalize_username(username):
    return username.strip().lower()


def build_expense_title(category, amount):
    return f"{category}: {format_amount(amount)}"


def get_default_user():
    return {
        "username": "ali",
        "password": "password"
    }
