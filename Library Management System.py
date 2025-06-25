import json
import os

DATA_FILE = "library_data.json"

# Initialize JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"books": [], "users": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- Book Operations ---
def add_book(data):
    book_id = input("Enter book ID: ").strip()
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if any(book["id"] == book_id for book in data["books"]):
        print("Book ID already exists.")
        return

    data["books"].append({"id": book_id, "title": title, "author": author})
    save_data(data)
    print("Book added successfully!")

def view_books(data):
    print("\n--- Book List ---")
    for book in data["books"]:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']}")
    if not data["books"]:
        print("No books available.")

def update_book(data):
    view_books(data)
    book_id = input("Enter book ID to update: ").strip()
    for book in data["books"]:
        if book["id"] == book_id:
            book["title"] = input("Enter new title: ").strip()
            book["author"] = input("Enter new author: ").strip()
            save_data(data)
            print("Book updated.")
            return
    print("Book ID not found.")

def delete_book(data):
    view_books(data)
    book_id = input("Enter book ID to delete: ").strip()
    for book in data["books"]:
        if book["id"] == book_id:
            data["books"].remove(book)
            save_data(data)
            print("Book deleted.")
            return
    print("Book ID not found.")

# --- User Operations ---
def add_user(data):
    user_id = input("Enter user ID: ").strip()
    name = input("Enter user name: ").strip()

    if any(user["id"] == user_id for user in data["users"]):
        print("User ID already exists.")
        return

    data["users"].append({"id": user_id, "name": name})
    save_data(data)
    print("User added successfully!")

def view_users(data):
    print("\n--- User List ---")
    for user in data["users"]:
        print(f"ID: {user['id']} | Name: {user['name']}")
    if not data["users"]:
        print("No users found.")

def update_user(data):
    view_users(data)
    user_id = input("Enter user ID to update: ").strip()
    for user in data["users"]:
        if user["id"] == user_id:
            user["name"] = input("Enter new name: ").strip()
            save_data(data)
            print("User updated.")
            return
    print("User ID not found.")

def delete_user(data):
    view_users(data)
    user_id = input("Enter user ID to delete: ").strip()
    for user in data["users"]:
        if user["id"] == user_id:
            data["users"].remove(user)
            save_data(data)
            print("User deleted.")
            return
    print("User ID not found.")

# --- Menu ---
def main():
    data = load_data()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add User")
        print("6. View Users")
        print("7. Update User")
        print("8. Delete User")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(data)
        elif choice == "2":
            view_books(data)
        elif choice == "3":
            update_book(data)
        elif choice == "4":
            delete_book(data)
        elif choice == "5":
            add_user(data)
        elif choice == "6":
            view_users(data)
        elif choice == "7":
            update_user(data)
        elif choice == "8":
            delete_user(data)
        elif choice == "9":
            print("Exiting... 📚")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
