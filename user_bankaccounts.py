# Create a User class with an __init__ method
class BankAccount:
    # Initializing the class BankAccount with a default balance of 0

    def __init__(self, balance=0):
        self.balance = balance
# Adding a make_deposit method to the User class

    def deposit(self, amount):
        self.balance += amount
        return self
# Add a make_withdrawal method to the User class

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self
# Adding a method to the User class that displays user's account balance

    def display_balance(self):
        return self.balance

# Initializing the User class with a name and a default bank account


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {'default': BankAccount()}
# Adding a method to make a deposit to a specified account

    def make_deposit(self, amount, account_name='default'):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Account {account_name} does not exist")
        return self
# Making a withdrawal from a specified account

    def make_withdrawal(self, amount, account_name='default'):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Account {account_name} does not exist")
        return self
# Displaying the balance of a specified account

    def display_user_balance(self, account_name='default'):
        if account_name in self.accounts:
            return self.accounts[account_name].display_balance()
        print(f"Account {account_name} does not exist")
        return None
# Adding a new account to the user

    def add_account(self, account_name):
        if account_name not in self.accounts:
            self.accounts[account_name] = BankAccount()
        else:
            print(f"Account {account_name} already exists")
# Transferring money between users and their specified accounts

    def transfer_money(self, amount, other_user, from_account='default', to_account='default'):
        if from_account in self.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].withdraw(amount)
                other_user.make_deposit(amount, to_account)
            else:
                print("Insufficient funds")
        else:
            print(f"Account {from_account} does not exist")
        return self

    # Creating users
user1 = User("Laz")
user2 = User("Ana")

# Making deposits
user1.make_deposit(1180)
user2.make_deposit(3050)

# Making withdrawals
user1.make_withdrawal(80)
user2.make_withdrawal(50)

# Displaying user balances
print(f"{user1.name}'s Checking Balance: ${user1.display_user_balance()}")
print(f"{user2.name}'s Savings Balance: ${user2.display_user_balance()}")
