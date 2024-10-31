from datetime import datetime

# Function to write a new diary entry
def write_entry():
    entry = input("What would you like to write in your diary today? ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"{timestamp} - {entry}\n")
    print("Entry added!")

# Function to read all diary entries
def read_entries():
    print("\nYour Diary Entries:")
    try:
        with open("diary.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No entries found. Start by writing your first entry!")

# Main menu
def diary_app():
    while True:
        print("\nDiary Menu:")
        print("1. Write a new entry")
        print("2. Read past entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye Teacher Gregory")
            break
        else:
            print("Invalid choice. Try again.")

# Run the app
diary_app()
