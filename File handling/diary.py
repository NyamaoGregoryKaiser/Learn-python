from datetime import datetime

# Password setup
PASSWORD = "nyamao"  # You can change this to any password you prefer

def authenticate():
    password = input("Enter your diary password: ")
    if password == PASSWORD:
        print("Access granted!\n")
        return True
    else:
        print("Access denied! Incorrect password.")
        return False

def write_entry():
    entry = input("Please enter what you would like to write in your diary: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp} - {entry}\n")
        print("Entry added!\n")

def read_entries():
    print("\nHere is your diary:")
    try:
        with open("diary.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No entries found. Start by writing your first entry!\n")

# Main diary function with password check
def diary_app():
    if not authenticate():
        return  # Exit if password is incorrect

    while True:
        print("\nYour Diary Menu:")
        print("1. Write a new entry")
        print("2. Read past entries")
        print("3. Exit")
        choice = input("Choose your option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye Teacher Gregory!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the diary app
diary_app()
