# Implement a BankAccount class with attributes like account_number and balance. Create a 
# subclass SavingsAccount that adds an attribute interest_rate and a method to calculate 
# interest.

class BankAccount:
    def __init__(self,acNo,balance):
        self.acNo = acNo 
        self.balance = balance


class SavingAccount(BankAccount):
    def __init__(self, acNo, balance,interest_rate):
        super().__init__(acNo, balance)
        self.interest_rate = interest_rate

    def calculate_Intrest(self):
        interest = self.balance * self.interest_rate / 100
        total_balance = self.balance + interest
        print(f"Intrest rate is {self.interest_rate}, interest amount is {interest} and total balance is {total_balance}")


account_no = int(input("Enter Account No:->"))
balance = int(input("Enter balance:->"))
interest = float(input("Enter interest rate (in percentage):->"))

s = SavingAccount(account_no,balance,interest)
s.calculate_Intrest()