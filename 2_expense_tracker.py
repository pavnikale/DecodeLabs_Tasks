print("Welcome to the Python Expense Tracker")
track = []

while True:
    print("1) Add expense")
    print("2) View expense")
    print("3) Quit")

    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        date = input("Enter Date: ")
        amt = int(input("Enter Amount: "))
        track.append("date": date, "amount": amt)
        print(track)
    elif choice == 2:
        print(track)
    else:
        break
