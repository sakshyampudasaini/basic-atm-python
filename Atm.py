correct_pin = 1234
balance = 0
pin = int(input("Enter your 4-digit PIN:-- "))

if pin == correct_pin:
    print("Welcome")

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4):-- ")

    if choice == "1":
        print(f"Your balance is{balance}")
    elif choice == "2":
        amount = int(input("Enter the amount to deposit:-- "))
        balance += amount
        print(f"Amount deposited successfully. The new amount is {balance}")
    elif choice == "3":
        amount = int(input("Enter the amount to withdraw:-- "))
        if amount <= balance:
            balance -= amount
            print(f"Withdraw done. The new amount is {balance}")
        else:
            print("Insufficient balance")
    elif choice == "4":
        print("Thank you for using the ATM")
    else:
        print("Invalid menu option")
else:
    print("Incorrect PIN")
