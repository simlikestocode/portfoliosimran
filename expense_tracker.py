import json
import os

FILE_NAME = "expenses.json"

# Load existing data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        expenses = json.load(f)
else:
    expenses = []

def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expenses.append({"name": name, "amount": amount})
    save_expenses()
    print("Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    total = 0
    print("\n--- Expenses ---")
    for e in expenses:
        print(f"{e['name']}: ${e['amount']}")
        total += e["amount"]

    print(f"\nTotal spent: ${total:.2f}")

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
