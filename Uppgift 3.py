# moment3.py
# Programming 1 – Moment 3: Assignment
# Loop-based Menu Program with Bonus

while True:
    print("\n==== MENU ====")
    print("1. Say hello")
    print("2. Show numbers 1–5")
    print("3. Multiply two numbers")
    print("4. Quit")
    print("5. Multiplication table (bonus)")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        for i in range(1, 6):
            print(i)

    elif choice == "3":
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"Result: {a * b}")
        except ValueError:
            print("Invalid input, please enter numbers only.")

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        try:
            num = int(input("Enter a number: "))
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Invalid input, please enter a number.")

    else:
        print("Please choose 1, 2, 3, 4, or 5")
