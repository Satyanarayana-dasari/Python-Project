import json
import os
from datetime import datetime

BLOG_FILE = "blog_data.json"

def load_posts():
    if not os.path.exists(BLOG_FILE):
        return []
    with open(BLOG_FILE, "r") as f:
        return json.load(f)

def save_posts(posts):
    with open(BLOG_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def create_post(posts):
    title = input("Enter post title: ").strip()
    content = input("Enter post content: ").strip()

    if not title or not content:
        print("Title and content cannot be empty.")
        return

    post = {
        "id": len(posts) + 1,
        "title": title,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    posts.append(post)
    save_posts(posts)
    print("Post created successfully!")

def view_posts(posts):
    if not posts:
        print("No blog posts found.")
        return
    print("\n--- Blog Posts ---")
    for post in posts:
        print(f"\nID: {post['id']}")
        print(f"📝 Title: {post['title']}")
        print(f"📅 Date: {post['date']}")
        print(f"📄 Content: {post['content']}\n{'-'*40}")

def delete_post(posts):
    view_posts(posts)
    try:
        post_id = int(input("Enter post ID to delete: "))
        for post in posts:
            if post["id"] == post_id:
                posts.remove(post)
                # Reassign IDs after deletion
                for i, p in enumerate(posts, 1):
                    p["id"] = i
                save_posts(posts)
                print("Post deleted.")
                return
        print("Post not found.")
    except ValueError:
        print("Invalid input.")

def main():
    posts = load_posts()
    while True:
        print("\n=== Simple Blog ===")
        print("1. Create Post")
        print("2. View Posts")
        print("3. Delete Post")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_post(posts)
        elif choice == "2":
            view_posts(posts)
        elif choice == "3":
            delete_post(posts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-4.")

if __name__ == "__main__":
    main()
