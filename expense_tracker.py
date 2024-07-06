import csv

"""Description: Create a command-line application to track daily expenses. 
Allow users to add, edit, and delete expense records. Save data in a CSV file."""

expenses_record: list = list()


def add_expenses():
    global expenses_record
    category: str = input("Enter your category: ")
    try:
        amount: float = float(input("Enter the amount: "))
    except ValueError:
        print("Enter a valid amount\n")
        return    
    expenses = {"category": category, "amount": amount}
    expenses_record.append(expenses)
    print("Expense added successfully!\n")

def edit_expenses():
    global expenses_record
    category: str = input("Enter category to edit: ")
    for expense in expenses_record:
        if expense["category"] == category:
            new_amount: float = float(input("Enter the new amount: "))
            expense["amount"] = new_amount
            print("Expense updated successfully!")
            return
    print("Category not found.\n")

def view_expenses():
    if not expenses_record:
        print("No expenses recorded.\n")
        return
    
    for i, expense in enumerate(expenses_record, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']} \n")    

def delete_expenses():
    global expenses_record
    category: str = input("Enter Expense to delete (Category): ")
    for i, expense in enumerate(expenses_record):
        if expense['category'] == category:
            del expenses_record[i]
            print(f"Expense '{category}' deleted successfully!\n")
            return
    print(f"Expense with category '{category}' not found.\n")

def save_expenses_to_csv(filename='expenses.csv'):
    global expenses_record
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['category', 'amount'])
        writer.writeheader()
        writer.writerows(expenses_record)
    print("Expenses saved to CSV file successfully!")


def main():
    global expenses_record
    while True:
        print("Expenses Tracker")
        print("******************\n")
        print("1.Add Expense")
        print("2.Edit Expense")
        print("3.View Expenses")
        print("4.Delete Expenses")
        print("5.Save Expenses as file")
        print("6.Exist")


        choose = input("Choose: ")

        if choose == "1":
            add_expenses()

        elif choose == "2":
            edit_expenses()

        elif choose == "3":
            view_expenses()

        elif choose == "4":
            delete_expenses() 

        elif choose == "5":
            save_expenses_to_csv() 

        elif choose == "6":
            print("Existing")
            break    

if __name__ == "__main__":
    main()