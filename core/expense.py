from datetime import datetime
from config.config import DATE_FORMAT


class Expense:

    def __init__(self, id, amount, category, note, username, created_at=None):
        self.id = str(id)
        self.amount = int(amount)
        self.category = category
        self.note = note
        self.username = username
        self.created_at = created_at or datetime.now().strftime(DATE_FORMAT)

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "username": self.username,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id", "0"),
            amount=data.get("amount", 0),
            category=data.get("category", "Boshqa"),
            note=data.get("note", ""),
            username=data.get("username", "unknown"),
            created_at=data.get("created_at")
        )

    def formatted_line(self, show_date=True):
        date_part = f" [{self.created_at}]" if show_date else ""
        return f"{self.id}. {self.category} - {self.amount} so'm ({self.note}){date_part}"

    def summary_line(self):
        return f"{self.category} - {self.amount} so'm"

    def matches_category(self, category):
        return self.category == category

    def update_note(self, new_note):
        self.note = new_note

    def update_category(self, new_category):
        self.category = new_category

    def age_in_days(self):
        try:
            created = datetime.strptime(self.created_at, DATE_FORMAT)
            delta = datetime.now() - created
            return delta.days
        except Exception:
            return 0

    def display_info(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "username": self.username,
            "created_at": self.created_at
        }
