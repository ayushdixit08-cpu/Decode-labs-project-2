print("===================================")
print("      EXPENSE TRACKER SYSTEM")
print("===================================")

total_expense = 0.0
expense_count = 0

while True:
    expense = input("\nEnter expense amount (or type 'quit' to finish): ")

    # Exit condition
    if expense.lower() in ["quit", "exit"]:
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative.")
            continue

        total_expense += expense
        expense_count += 1

        print(f"Expense Added : ₹{expense:.2f}")
        print(f"Current Total : ₹{total_expense:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

print("\n===================================")
print("        EXPENSE SUMMARY")
print("===================================")
print(f"Total Expenses Entered : {expense_count}")
print(f"Total Amount Spent     : ₹{total_expense:.2f}")

if expense_count > 0:
    average = total_expense / expense_count
    print(f"Average Expense        : ₹{average:.2f}")
else:
    print("No expenses were entered.")

print("Thank you for using Expense Tracker!")