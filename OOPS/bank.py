class BankAccount:

    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0
    
    def deposit(self):
        depAmt = int(input("Enter Amount for deposit:->"))
        self.balance += depAmt
        print(f"Deposited amount is {depAmt} and balance in your account is {self.balance}") 
    
    def withdrawal(self):
        withdrawalAmt = int(input("Enter amount for withdrawal:->"))

        if withdrawalAmt <= self.balance:
            self.balance -= withdrawalAmt
            print(f"Withdrawn amount is {withdrawalAmt} and balance in your account is {self.balance}") 
        else:
            print("Oops! Insufficient balance.")

    def amtCheck(self):
        print(f"Remaining balance in your account is {self.balance}")


account_no = int(input("Enter Account NUmber:->"))

bank_Ac = BankAccount(account_no)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Account amount")
    print("4. Exit")

    choice = int(input("Enter your choice:->"))

    if choice == 1:
        bank_Ac.deposit() 
    elif choice == 2:
        bank_Ac.withdrawal()
    elif choice == 3:
        bank_Ac.amtCheck()
    elif choice == 4:
        print("Exiting the bank account system.")
        break 
    else:
        print("Invalid choice. Please enter a valid option.")
