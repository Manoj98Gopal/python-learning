# A private member in Python is a variable ot method that is defined using double underscores.
# It is used to restrict direct access from outside the class

class BankAccount:

    def __init__(self, name, balance):
        self.name = name  # public attributes
        self.__balance = balance  # private attributes

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        self.__balance += amount
        print('Amount deposited successfully')


account = BankAccount("Manoj", 5000)

print(account.name)
print(account.get_balance())
account.deposite(200)
print(account.get_balance())
