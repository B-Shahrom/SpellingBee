import random
import os
from pathlib import Path

FILENAME = "names.txt"
FILE_DIRECTORY = str(Path(__file__).parent) + '\\' + FILENAME

def ensure_file_exists():
    """Create the file if it doesn't exist."""
    if not os.path.exists(FILE_DIRECTORY):
        with open(FILE_DIRECTORY, "w", encoding="utf-8") as f:
            pass  # create empty file

def read_names():

    """Read all names from the file."""
    ensure_file_exists()
    with open(FILE_DIRECTORY, "r", encoding="utf-8") as file:
        names = [line.strip() for line in file if line.strip()]
    if not names:
        print("\nNo names found in the file.")

    return names

def add_name(new_name):
    """Add a new name to the file."""
    ensure_file_exists()
    with open(FILE_DIRECTORY, "a", encoding="utf-8") as file:
        file.write(new_name + "\n")
    print(f"✅ Added '{new_name}' to {FILE_DIRECTORY}")

def remove_name(name_to_remove):
    """Remove a name from the file."""
    names = read_names()
    if not names:
        return
    if name_to_remove not in names:
        print(f"⚠️ '{name_to_remove}' not found in the file.")
        return
    names.remove(name_to_remove)
    with open(FILE_DIRECTORY, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")
    print(f"🗑 Removed '{name_to_remove}' successfully.")

def select_random_name():
    """Select and print a random name from the file."""
    names = read_names()
    if not names:
        return
    chosen = random.choice(names)
    return chosen
    #print(f"\n🎲 Randomly selected name: {chosen}")

def main():
    ensure_file_exists()
    while True:
        print("\n=== Name Manager ===")
        print("1. View all names")
        print("2. Add a new name")
        print("3. Remove a name")
        print("4. Pick a random name")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            read_names()
        elif choice == "2":
            new_name = input("Enter a new name: ").strip()
            if new_name:
                add_name(new_name)
            else:
                print("⚠️ Name cannot be empty.")
        elif choice == "3":
            name_to_remove = input("Enter the name to remove: ").strip()
            if name_to_remove:
                remove_name(name_to_remove)
            else:
                print("⚠️ Name cannot be empty.")
        elif choice == "4":
            select_random_name()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again.")

if __name__ == "__main__":
    pass
