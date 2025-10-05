expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Total Spent\n4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        item = input("Enter item name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"item": item, "amount": amount})
    elif choice == '2':
        for e in expenses:
            print(f"{e['item']}: ${e['amount']:.2f}")
    elif choice == '3':
        total = sum(e['amount'] for e in expenses)
        print(f"Total spent: ${total:.2f}")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")