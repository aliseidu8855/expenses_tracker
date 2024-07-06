import csv

"""Description: Create a command-line application to track daily expenses. 
Allow users to add, edit, and delete expense records. Save data in a CSV file."""

def load_expenses_from_csv(filename='expenses.csv'):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            expenses_record = [row for row in reader]
            for expense in expenses_record:
                expense['amount'] = float(expense['amount'])  # Convert amount to float
        print("Expenses loaded from CSV file successfully!")
    except FileNotFoundError:
        print("No existing CSV file found. Starting with an empty expense record.\n")
        expenses_record = []
    return expenses_record

def add_expenses(expenses_record):
    category = input("Enter your category: ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Enter a valid amount\n")
        return    
    expenses = {"category": category, "amount": amount}
    expenses_record.append(expenses)
    print("Expense added successfully!\n")

def edit_expenses(expenses_record):
    category = input("Enter category to edit: ")
    for expense in expenses_record:
        if expense["category"] == category:
            try:
                new_amount = float(input("Enter the new amount: "))
                expense["amount"] = new_amount
                print("Expense updated successfully!\n")
                return
            except ValueError:
                print("Enter a valid amount\n")
                return
    print("Category not found.\n")

def view_expenses(expenses_record):
    if not expenses_record:
        print("No expenses recorded.\n")
        return
    
    for i, expense in enumerate(expenses_record, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']} \n")    

def delete_expenses(expenses_record):
    category = input("Enter Expense to delete (Category): ")
    for i, expense in enumerate(expenses_record):
        if expense['category'] == category:
            del expenses_record[i]
            print(f"Expense '{category}' deleted successfully!\n")
            return
    print(f"Expense with category '{category}' not found.\n")

def save_expenses_to_csv(expenses_record, filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['category', 'amount'])
        writer.writeheader()
        writer.writerows(expenses_record)
    print("Expenses saved to CSV file successfully!")

def main():
    expenses_record = load_expenses_from_csv() 
    while True:
        print("Expenses Tracker")
        print("******************\n")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. View Expenses")
        print("4. Delete Expenses")
        print("5. Save Expenses as file")
        print("6. Exit")

        choose = input("Choose: ")

        if choose == "1":
            add_expenses(expenses_record)
        elif choose == "2":
            edit_expenses(expenses_record)
        elif choose == "3":
            view_expenses(expenses_record)
        elif choose == "4":
            delete_expenses(expenses_record)
        elif choose == "5":
            save_expenses_to_csv(expenses_record)
        elif choose == "6":
            save_expenses_to_csv(expenses_record)  
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    main()
