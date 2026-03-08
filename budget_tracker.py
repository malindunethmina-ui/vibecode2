def main():
    print("--- Monthly Budget Tracker ---")
    
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        # Ask for expenses until 'done' is entered
        expenses = []
        while True:
            entry = input("Enter an expense (or type 'done' to finish): ").strip().lower()
            if entry == 'done':
                break
            try:
                expense = float(entry)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a numeric value or 'done'.")
        
        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Display remaining balance
        print(f"\nTotal Budget:   LKR {total_budget:,.2f}")
        print(f"Total Expenses: LKR {total_expenses:,.2f}")
        print(f"Remaining Balance: LKR {remaining_balance:,.2f}")
        
        if remaining_balance < 500:
            print("Warning: Low Funds")
            
        input("\nPress Enter to exit...")
            
    except ValueError:
        print("Invalid input. Please enter numeric values for budget and expenses.")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
