balance = 1000

while True:
    print("\n--- MENU ---")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Try again.")
                continue

            if amount > balance:
                print("Error: Insufficient funds!")

                print("\nOptions:")
                print("1. Try again")
                print("2. Check balance")
                print("3. Exit")

                option = input("Choose an option: ")

                if option == "1":
                    continue
                elif option == "2":
                    print(f"Current balance: {balance}")
                elif option == "3":
                    print("Exiting program...")
                    break
                else:
                    print("Invalid option.")

            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: {balance}")

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == "2":
        print(f"Current balance: {balance}")

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")