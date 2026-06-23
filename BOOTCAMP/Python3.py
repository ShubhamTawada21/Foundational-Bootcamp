import random
import sys

class ATM:
    def __init__(self):

        self.accounts = {
            "123456": {"pin": "1111", "balance": 500.0, "history": ["Initial Deposit: $500.00"]},
        }
        self.current_user = None

    def main_menu(self):
        """Initial welcome screen for card insertion or account creation."""
        while True:
            print("\n" + "="*30)
            print("    WELCOME TO THE TECH BANK    ")
            print("="*30)
            print("1. Insert Card (Log In)")
            print("2. Open Account & Generate PIN")
            print("3. Power Off ATM")
            print("="*30)
            
            choice = input("Please select an option (1-3): ").strip()
            
            if choice == "1":
                self.login()
            elif choice == "2":
                self.generate_pin_and_account()
            elif choice == "3":
                print("\nShutting down ATM system. Goodbye!")
                sys.exit()
            else:
                print(" Invalid choice. Please enter 1, 2, or 3.")

    def generate_pin_and_account(self):
        """Feature: Creates a new unique account and lets the user generate/set their PIN."""
        print("\n--- Account Creation & PIN Generation ---")

        while True:
            new_acc = str(random.randint(100000, 999999))
            if new_acc not in self.accounts:
                break
        

        while True:
            pin = input("Set your new 4-digit PIN: ").strip()
            if len(pin) == 4 and pin.isdigit():
                confirm_pin = input("Confirm your 4-digit PIN: ").strip()
                if pin == confirm_pin:
                    break
                else:
                    print(" PINs do not match. Try again.")
            else:
                print(" Invalid PIN format! PIN must be exactly 4 digits.")

        while True:
            try:
                initial_deposit = float(input("Enter initial deposit amount to activate account: $"))
                if initial_deposit >= 0:
                    break
                print(" Deposit cannot be negative.")
            except ValueError:
                print(" Invalid input. Please enter a valid amount.")

        self.accounts[new_acc] = {
            "pin": pin,
            "balance": initial_deposit,
            "history": [f"Account opened with initial deposit: ${initial_deposit:.2f}"]
        }
        print(f"\n Account successfully created! Please log in using Account Number: {new_acc}")

    def login(self):
        """Feature: Handles Account authentication, Correct PIN, and Invalid PIN checks."""
        print("\n--- User Login ---")
        acc_num = input("Enter your 6-digit Account Number: ").strip()

        if acc_num not in self.accounts:
            print(" Invalid Account Number. Access Denied.")
            return

        attempts = 3
        while attempts > 0:
            pin_input = input(f"Enter your 4-digit PIN ({attempts} attempts remaining): ").strip()

            if self.accounts[acc_num]["pin"] == pin_input:
                print("\n PIN Verified successfully!")
                self.current_user = acc_num
                self.atm_operations_menu()
                return

            else:
                attempts -= 1
                print(" Incorrect PIN.")
        
        print("\n Security Alert: Too many incorrect PIN attempts. This account is locked for safety!")

    def atm_operations_menu(self):
        """The core banking menu once logged in."""
        acc = self.current_user
        while True:
            print("\n" + "~"*25)
            print(f"   ACCOUNT: {acc}   ")
            print("~"*25)
            print("1. View Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. View Statement History")
            print("5. Logout / Exit")
            print("~"*25)
            
            choice = input("Select an action (1-5): ").strip()

            if choice == "1":
                balance = self.accounts[acc]["balance"]
                print(f"\n Your Current Balance is: ${balance:.2f}")

            elif choice == "2":
                try:
                    amount = float(input("\nEnter withdrawal amount: $"))
                    if amount <= 0:
                        print(" Amount must be greater than zero.")
                    elif amount > self.accounts[acc]["balance"]:
                        print(" Transaction Declined: Insufficient funds!")
                    else:
                        self.accounts[acc]["balance"] -= amount
                        self.accounts[acc]["history"].append(f"Withdrew: ${amount:.2f}")
                        print(f" Cash Dispensed! Please collect your ${amount:.2f}")
                        print(f"Remaining Balance: ${self.accounts[acc]['balance']:.2f}")
                except ValueError:
                    print(" Invalid input format. Please enter a valid number.")

            elif choice == "3":
                try:
                    amount = float(input("\nEnter deposit amount: $"))
                    if amount > 0:
                        self.accounts[acc]["balance"] += amount
                        self.accounts[acc]["history"].append(f"Deposited: ${amount:.2f}")
                        print(f" Success! Your new balance is: ${self.accounts[acc]['balance']:.2f}")
                    else:
                        print(" Invalid deposit amount.")
                except ValueError:
                    print(" Invalid input format.")

            elif choice == "4":
                print("\n--- Recent Transactions ---")
                for transaction in self.accounts[acc]["history"]:
                    print(f"• {transaction}")

            elif choice == "5":
                print("\n Session closed. Card ejected safely.")
                self.current_user = None
                break
            else:
                print(" Invalid option.")

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()