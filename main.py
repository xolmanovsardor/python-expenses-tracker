# Sodda xarajatlar boshqaruv dasturi

from config.config import CATEGORIES, MAX_LOGIN_ATTEMPTS, normalize_username
from core.manager import ExpenseManager
from utils.security import SecurityManager
from utils.utils import clear_screen, print_header, prompt_int, prompt_non_empty


def show_menu():
    print_header("MENU")
    print("1. Xarajat qo'shish")
    print("2. Xarajatlarni ko'rish")
    print("3. Kategoriya bo'yicha filter")
    print("4. Statistika")
    print("5. Xarajatni o'chirish")
    print("0. Chiqish")


def show_category_menu():
    print("Kategoriyalar:")
    for index, category in enumerate(CATEGORIES, 1):
        print(f"{index}. {category}")


def select_category():
    show_category_menu()
    choice = prompt_int("Tanlang: ", min_value=1, max_value=len(CATEGORIES))
    if choice is None:
        print("Raqam kiriting!")
        return None
    return CATEGORIES[choice - 1]


def add_expense_ui(manager):
    amount = prompt_int("Summa: ", min_value=1)
    if amount is None:
        print("Summa xato! Iltimos, musbat raqam kiriting.")
        return

    category = select_category()
    if category is None:
        return

    note = prompt_non_empty("Izoh: ")
    if note is None:
        print("Izoh bo'sh bo'lishi mumkin emas.")
        return

    manager.add_expense(amount, category, note)
    print(f"Xarajat qo'shildi: {category} - {amount} so'm")


def filter_ui(manager):
    category = select_category()
    if category is None:
        return

    filtered = manager.filter_by_category(category)
    if not filtered:
        print(f"{category} kategoriyasida xarajat yo'q")
        return

    print_header(f"{category} KATEGORIYASI")
    for expense in filtered:
        print(expense.formatted_line())


def delete_expense_ui(manager):
    expense_id = prompt_int("O'chirmoqchi bo'lgan xarajat ID sini kiriting: ", min_value=1)
    if expense_id is None:
        print("Noto'g'ri ID.")
        return

    if manager.remove_expense(expense_id):
        print("Xarajat muvaffaqiyatli o'chirildi.")
    else:
        print("Bunday ID bilan xarajat topilmadi.")


def show_auth_menu():
    print_header("KIRISH / RO'YXATDAN O'TISH")
    print("1. Kirish")
    print("2. Ro'yxatdan o'tish")
    print("0. Chiqish")


def register_user():
    print_header("RO'YXATDAN O'TISH")
    while True:
        username = prompt_non_empty("Yangi login: ")
        if username is None:
            print("Login bo'sh bo'lmasin.")
            continue

        if SecurityManager.find_user(username):
            print("Bu login band. Iltimos, boshqasini tanlang.")
            continue

        password = prompt_non_empty("Yangi parol: ")
        if password is None or len(password) < 4:
            print("Parol kamida 4 ta belgidan iborat bo'lishi kerak.")
            continue

        confirm = prompt_non_empty("Parolni qayta kiriting: ")
        if confirm != password:
            print("Parollar mos kelmadi. Qaytadan urinib ko'ring.")
            continue

        if SecurityManager.add_user(username, password):
            print("✅ Ro'yxatdan o'tish muvaffaqiyatli.")
            return normalize_username(username)

        print("Ro'yxatdan o'tishda xatolik yuz berdi.")
        return None


def login():
    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = prompt_non_empty("Foydalanuvchi nomi: ")
        password = prompt_non_empty("Parol: ")

        if username is None or password is None:
            print("Iltimos, barcha maydonlarni to'ldiring.")
            attempts += 1
            continue

        if SecurityManager.authenticate(username, password):
            print(f"✅ Xush kelibsiz, {normalize_username(username).title()}!")
            return normalize_username(username)

        attempts += 1
        remaining = SecurityManager.login_attempts_remaining(attempts)
        print(f"❌ Noto'g'ri login yoki parol. Qolgan urinish: {remaining}")

    print("Kirish urinishlari tugadi.")
    return None


def auth_menu():
    while True:
        show_auth_menu()
        choice = input("Tanlang: ")

        if choice == "1":
            username = login()
            if username:
                return username
        elif choice == "2":
            username = register_user()
            if username:
                return username
        elif choice == "0":
            return None
        else:
            print("Xato tanlov!")


def main():
    clear_screen()
    print("XARAJATLAR BOSHQARUV DASTURI")

    username = auth_menu()
    if not username:
        return

    manager = ExpenseManager(username)

    while True:
        show_menu()
        choice = input("Tanlang: ")

        if choice == "1":
            add_expense_ui(manager)
        elif choice == "2":
            expenses = manager.list_expenses()
            if not expenses:
                print("Xarajatlar yo'q")
            else:
                print_header("XARAJATLAR")
                for exp in expenses:
                    print(exp.formatted_line())
        elif choice == "3":
            filter_ui(manager)
        elif choice == "4":
            stats = manager.show_stats()
            print_header("STATISTIKA")
            print(f"Jami: {stats['total']} so'm")
            if stats['top_category']:
                print(f"Top kategoriya: {stats['top_category']} - {stats['top_amount']} so'm")
        elif choice == "5":
            delete_expense_ui(manager)
        elif choice == "0":
            print("Xayr!")
            break
        else:
            print("Xato tanlov!")


if __name__ == "__main__":
    main()
