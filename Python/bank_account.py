# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance_attribute=0.0):
        self.owner = owner
        self.balance_attribute = balance_attribute

    def deposit(self, amount):
        self.balance_attribute += amount
        return self.balance_attribute

    def withdraw(self,amount):
        self.balance_attribute -= amount
        return self.balance_attribute

user1 = BankAccount("Bobba Fett")
user1.deposit(10)
print(user1.balance_attribute)
