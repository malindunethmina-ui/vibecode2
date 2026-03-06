def calculate_grade():
    # Ask for student's name
    name = input("Enter student's name: ")

    try:
        # Ask for 3 subject marks
        mark1 = float(input("Enter marks for subject 1: "))
        mark2 = float(input("Enter marks for subject 2: "))
        mark3 = float(input("Enter marks for subject 3: "))

        # Calculate the average
        average = (mark1 + mark2 + mark3) / 3

        print(f"\nStudent Name: {name}")
        print(f"Average Mark: {average:.2f}")

        # Assign Grades based on average
        if average >= 75:
            print("Grade: A")
        elif average >= 60:
            print("Grade: B")
        elif average >= 40:
            print("Grade: C")
        else:
            print("Status: Fail")

        # Keep the window open
        input("\nPress Enter to exit...")

    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    calculate_grade()
