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

#account 1
account1 = BankAccount(0.07, 400)
account1.deposit(100).yield_interest().display_account_info().withdraw(200).display_account_info

#account 2
account2 = BankAccount(0.03, 0)
account2.withdraw(1000).display_account_info().yield_interest().display_account_info()