from src import customer
from src import billing
from src import eligibility


def print_menu():
    print()
    print("=" * 60)
    print("MAIN MENU")
    print("=" * 60)
    print("1. Customer Profile and Financial Summary")
    print("2. Product Billing Calculator")
    print("3. Loan Eligibility Decision")
    print("4. Campaign Eligibility Checker")
    print("5. Exit")


def main():
    print("Welcome to the Customer Evaluation and Decision Support System")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            customer.run()
        elif choice == "2":
            billing.run()
        elif choice == "3":
            eligibility.run_loan_eligibility()
        elif choice == "4":
            eligibility.run_campaign_eligibility()
        elif choice == "5":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("  -> Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
