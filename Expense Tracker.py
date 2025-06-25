import json
import os

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"transactions": [], "balance": 0.0}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(data, type_):
    try:
        amount = float(input(f"Enter {type_} amount: ₹ "))
        description = input("Enter description: ").strip()
        if amount <= 0:
            print("Amount must be positive.")
            return
        if type_ == "expense":
            amount = -amount
        transaction = {"type": type_, "amount": amount, "description": description}
        data["transactions"].append(transaction)
        data["balance"] += amount
        save_data(data)
        print(f"{type_.capitalize()} recorded successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_transactions(data):
    if not data["transactions"]:
        print("No transactions recorded.")
        return
    print("\n--- Transaction History ---")
    for i, t in enumerate(data["transactions"], 1):
        type_icon = "💰" if t["type"] == "income" else "💸"
        print(f"{i}. {type_icon} {t['type'].capitalize()}: ₹{abs(t['amount'])} - {t['description']}")
    print(f"\n💼 Current Balance: ₹{data['balance']:.2f}")

def main():
    data = load_data()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(data, "income")
        elif choice == "2":
            add_transaction(data, "expense")
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            print("Exiting... 💼")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
