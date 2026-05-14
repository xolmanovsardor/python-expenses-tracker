from core.expense import Expense
from utils.utils import FileUtils
from config.config import CATEGORIES


class ExpenseManager:

    def __init__(self, username):
        self.username = username
        self.expenses = FileUtils.load_expenses()
        self.user_expenses = self._load_user_expenses()

    def _load_user_expenses(self):
        return [exp for exp in self.expenses if exp.get("username") == self.username]

    def add_expense(self, amount, category, note):
        if category not in CATEGORIES:
            raise ValueError("Noto'g'ri kategoriya")

        new_id = FileUtils.get_next_id(self.expenses)
        expense = Expense(
            id=new_id,
            amount=amount,
            category=category,
            note=note,
            username=self.username
        )
        expense_dict = expense.to_dict()
        self.expenses.append(expense_dict)
        self.user_expenses.append(expense_dict)
        FileUtils.save_expenses(self.expenses)

        return expense

    def list_expenses(self):
        return [Expense.from_dict(exp) for exp in self.user_expenses]

    def filter_by_category(self, category):
        return [Expense.from_dict(exp) for exp in self.user_expenses if exp.get("category") == category]

    def find_expense(self, expense_id):
        for exp in self.user_expenses:
            if str(exp.get("id")) == str(expense_id):
                return Expense.from_dict(exp)
        return None

    def remove_expense(self, expense_id):
        target = None
        for exp in self.expenses:
            if str(exp.get("id")) == str(expense_id) and exp.get("username") == self.username:
                target = exp
                break

        if not target:
            return False

        self.expenses.remove(target)
        self.user_expenses = self._load_user_expenses()
        FileUtils.save_expenses(self.expenses)
        return True

    def show_stats(self):
        if not self.user_expenses:
            return {
                "total": 0,
                "top_category": None,
                "category_sum": {}
            }

        total = sum(exp.get("amount", 0) for exp in self.user_expenses)
        category_sum = {}
        for exp in self.user_expenses:
            cat = exp.get("category")
            category_sum[cat] = category_sum.get(cat, 0) + exp.get("amount", 0)

        top_category = max(category_sum, key=category_sum.get)
        return {
            "total": total,
            "top_category": top_category,
            "top_amount": category_sum[top_category],
            "category_sum": category_sum
        }
