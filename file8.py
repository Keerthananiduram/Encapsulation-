




class BankAccount:

    def __init__(self, owner, bal): #prvt
        self.owner = owner
        self.__bal = bal

    def get_balance(self):
        return self.__bal

    def deposite(self, amount):
        if amount > 0:
            self.__bal = self.__bal + amount

abc = BankAccount("kittu", 100)

print(abc.get_balance())

abc.deposite(50)

print(abc.get_balance())
