import json
import os

FILE_NAME = "notes.json"

# Load notes
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        notes = json.load(f)
else:
    notes = []

def save_notes():
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    save_notes()
    print("Note added!")

def view_notes():
    if not notes:
        print("No notes yet.")
        return

    print("\n--- Your Notes ---")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def delete_note():
    view_notes()
    try:
        index = int(input("\nEnter note number to delete: ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            save_notes()
            print(f"Deleted: {removed}")
        else:
            print("Invalid number")
    except:
        print("Please enter a valid number")

while True:
    print("\nNotes App")
    print("1. Add note")
    print("2. View notes")
    print("3. Delete note")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
