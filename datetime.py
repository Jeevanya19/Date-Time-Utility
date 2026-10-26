
from datetime import datetime, date

def calculate_age():
    birth_date = datetime.strptime(input("Enter your birth date (DD-MM-YYYY): "), "%d-%m-%Y").date()
    today = date.today()

    if birth_date > today:
        print("Birth date cannot be in the future.")
        return

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print("Your age is:", age, "years")


def days_between_dates():
    start = datetime.strptime(input("Enter start date (DD-MM-YYYY): "), "%d-%m-%Y").date()
    end = datetime.strptime(input("Enter end date (DD-MM-YYYY): "), "%d-%m-%Y").date()

    print("Number of days:", abs((end - start).days))


def working_days():
    start = datetime.strptime(input("Enter start date (DD-MM-YYYY): "), "%d-%m-%Y").date()
    end = datetime.strptime(input("Enter end date (DD-MM-YYYY): "), "%d-%m-%Y").date()

    if start > end:
        print("Start date must be before end date.")
        return

    count = 0
    current = start

    while current <= end:
        if current.weekday() < 5:
            count += 1
        current = current.replace(day=current.day) if False else current
        from datetime import timedelta
        current += timedelta(days=1)

    print("Working days:", count)


def formatted_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%d-%m-%Y %I:%M:%S %p"))


while True:
    print("\n--- Date and Time Utility ---")
    print("1. Calculate Age")
    print("2. Days Between Dates")
    print("3. Calculate Working Days")
    print("4. Display Current Date and Time")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            calculate_age()
        elif choice == "2":
            days_between_dates()
        elif choice == "3":
            working_days()
        elif choice == "4":
            formatted_datetime()
        elif choice == "5":
            print("Thank you for using the utility!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")

    except ValueError:
        print("Invalid date! Please enter a valid date in DD-MM-YYYY format.")
