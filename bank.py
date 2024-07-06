class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdraw amount or insufficient funds.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest: {interest}. New balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdraw amount or overdraft limit exceeded.")

# Example usage
print("Savings Account Example")
savings_account = SavingsAccount('SA12345', 'Alice', 1000.0)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.add_interest()
savings_account.get_balance()

print("\nCurrent Account Example")
current_account = CurrentAccount('CA12345', 'Bob', 1000.0)
current_account.deposit(500)
current_account.withdraw(200)
current_account.withdraw(1500)  # Overdraft
current_account.get_balance()
