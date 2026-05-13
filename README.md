# 💰 Mini Expense Tracker

### Soddalashtirilgan Texnik Topshiriq

---

# 1. Loyiha haqida

Terminalda ishlaydigan oddiy xarajatlar boshqaruv dasturi.

Foydalanuvchi:

* xarajat qo‘shadi
* xarajatlarni ko‘radi
* kategoriya bo‘yicha filtrlaydi
* umumiy statistikani ko‘radi

Ma’lumotlar `expenses.json` faylida saqlanadi.

---

# 2. Texnologiyalar

| Element   | Qiymat                 |
| --------- | ---------------------- |
| Til       | Python 3               |
| Paradigma | OOP                    |
| Storage   | JSON                   |
| Interface | CLI                    |
| Kutubxona | Faqat standard library |

---

# 3. Asosiy funksiyalar

## Xarajat qo‘shish

User quyidagilarni kiritadi:

* summa
* kategoriya
* izoh

Misol:

```python
100000
Oziq-ovqat
Tushlik
```

---

## Xarajatlarni ko‘rish

Barcha xarajatlar chiqariladi:

```text
1. Oziq-ovqat - 100000 so'm
2. Transport - 25000 so'm
```

---

## Kategoriya bo‘yicha filter

Masalan:

```text
Transport
```

Natija:

```text
Transport - 25000
Transport - 18000
```

---

## Statistikani ko‘rish

Ko‘rsatilsin:

* jami xarajat
* eng ko‘p ishlatilgan kategoriya

Misol:

```text
Jami: 560000 so'm

Top kategoriya:
Oziq-ovqat - 320000 so'm
```

---

# 4. Kategoriyalar

Faqat shu kategoriyalar ishlasin:

```python
CATEGORIES = [
    "Oziq-ovqat",
    "Transport",
    "Kiyim",
    "Ko'ngilochar",
    "Boshqa"
]
```

---

# 5. JSON struktura

## expenses.json

```json
[
    {
        "id": "1",
        "amount": 100000,
        "category": "Oziq-ovqat",
        "note": "Tushlik"
    }
]
```

---

# 6. Klasslar

## Expense klassi

```python
class Expense:
    def __init__(self, id, amount, category, note):
        self.id = id
        self.amount = amount
        self.category = category
        self.note = note
```

---

## ExpenseManager klassi

Bu klass:

* fayldan o‘qiydi
* faylga yozadi
* expense qo‘shadi
* list qaytaradi
* statistikani hisoblaydi

### Methodlar

| Method               | Vazifa               |
| -------------------- | -------------------- |
| load_expenses()      | JSON o‘qish          |
| save_expenses()      | JSON yozish          |
| add_expense()        | Xarajat qo‘shish     |
| list_expenses()      | Barchasini chiqarish |
| filter_by_category() | Filter               |
| show_stats()         | Statistika           |

---

# 7. Fayl strukturasi

```text
expense_tracker/
│
├── main.py
├── expense.py
├── manager.py
├── config.py
├── expenses.json
└── utils.py
```

---

# 8. Menu

```text
1. Xarajat qo'shish
2. Xarajatlarni ko'rish
3. Kategoriya bo'yicha filter
4. Statistika
0. Chiqish
```

---

# 9. Validatsiya

## Summa

Manfiy bo‘lmasin:

```python
if amount <= 0:
    print("Summa musbat bo'lishi kerak")
```

---

## Kategoriya

Faqat ro‘yxatdagilar ishlasin.

---

# 10. Bosqichlar

## 1-bosqich

* project ochish
* json fayl yaratish
* menu qilish

---

## 2-bosqich

* Expense klassi
* add expense

---

## 3-bosqich

* JSON save/load

---

## 4-bosqich

* filter
* statistika

---

# 11. Qabul kriteriyalari

* JSON saqlanishi ishlashi kerak
* dastur qayta ochilganda data qolishi kerak
* category validation ishlashi kerak
* manfiy summa qabul qilinmasligi kerak
* OOP ishlatilgan bo‘lishi kerak

---

# 12. Bonus

Qo‘shimcha qilish mumkin:

* sana qo‘shish
* expense delete
* monthly report
* ANSI color
* txt export

---

# 13. Minimal natija

User quyidagini qila olsa loyiha tayyor:

✅ xarajat qo‘shish
✅ xarajatlarni ko‘rish
✅ JSON saqlash
✅ filter
✅ statistika
