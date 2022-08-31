class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        info = self.__dict__
        for key in info:
            print(f"{key}: {info[key]}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def yield_user_interest(self):
        self.account.yield_interest()
        return self

    def display_user_account_info(self):
        self.account.display_account_info()
        return self


user1 = User("Weyland", "Yutani")
user1.display_user_account_info().make_deposit(50).display_user_account_info().yield_user_interest().display_user_account_info().make_withdrawal(25).display_user_account_info()

