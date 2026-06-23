class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)
        
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Deposit failed: Cannot deposit an amount of ${amount:.2f}. Must be greater than 0.")
        self.balance += amount
        print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return self.balance
        
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal failed: Cannot withdraw an amount of ${amount:.2f}. Must be greater than 0.")
        if amount > self.balance:
            raise InsufficientFundsError(f"Withdrawal failed: Attempted to withdraw ${amount:.2f}, but current balance is only ${self.balance:.2f}.")
            
        self.balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return self.balance


if __name__ == "__main__":
    print("\n--- Testing Bank Account Simulator ---")
    account = BankAccount("John Doe", initial_balance=100.00)
    
    try:
        account.deposit(50.0)
        account.withdraw(30.0)
    except (InvalidAmountError, InsufficientFundsError) as e:
        print(f"Caught an unexpected error: {e}")
        
    try:
        print("\nAttempting to deposit a negative amount...")
        account.deposit(-20.0)
    except InvalidAmountError as e:
        print(f"Caught Expected Exception: {e}")
        
    try:
        print("\nAttempting to overdraw...")
        account.withdraw(500.0)
    except InsufficientFundsError as e:
        print(f"Caught Expected Exception: {e}")                                        