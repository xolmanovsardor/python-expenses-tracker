import json
import os
from config.config import JSON_FILE


class FileUtils:
    """Fayllar bilan ishlash uchun yordamchi funksiyalar."""

    @staticmethod
    def load_expenses():
        """expenses.json fayldan xarajatlar ro'yxatini o'qiydi."""
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    @staticmethod
    def save_expenses(expenses_list):
        """Xarajatlarni expenses.json faylga yozadi."""
        directory = os.path.dirname(JSON_FILE)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump(expenses_list, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_next_id(expenses_list):
        """Keyingi ID raqamini aniqlaydi."""
        if not expenses_list:
            return 1

        try:
            max_id = max(int(exp.get("id", 0)) for exp in expenses_list)
        except ValueError:
            max_id = 0

        return max_id + 1


def clear_screen():
    """Terminal ekranini tozalaydi."""
    os.system("cls" if os.name == "nt" else "clear")


def print_divider(symbol="=", length=50):
    """Chiziq ajratgichini chiqaradi."""
    print(symbol * length)


def print_header(title):
    """Sarlavhali bo'lim matnini chiqaradi."""
    print_divider()
    print(title)
    print_divider()


def prompt_int(message, min_value=None, max_value=None):
    """Foydalanuvchidan butun son so'raydi."""
    try:
        value = int(input(message))
        if min_value is not None and value < min_value:
            raise ValueError
        if max_value is not None and value > max_value:
            raise ValueError
        return value
    except ValueError:
        return None


def prompt_non_empty(message):
    """Foydalanuvchidan bo'sh bo'lmagan satr so'raydi."""
    value = input(message).strip()
    return value if value else None
