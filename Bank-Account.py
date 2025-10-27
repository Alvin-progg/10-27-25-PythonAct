class BankAccount:

        def __init__(self, account_holder, __initial_balance=0):
            self.account_holder = account_holder
            self.balance = __initial_balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                return True
            return False

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                return True
            return False

        def get_balance(self):
            return self.balance

        def get_account_holder(self):
            return self.account_holder

if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    print(f"Account Holder: {account.get_account_holder()}")
    print(f"Initial Balance: {account.get_balance()}")

    account.deposit(500)
    print(f"Balance after deposit: {account.get_balance()}")

    account.withdraw(200)
    print(f"Balance after withdrawal: {account.get_balance()}")



