class BankAccount():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    #Deposit Money
    def deposit_money(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited in your bank. New Balance is {self.balance}")
        else:
            print("Deposit amount should be positive")
    #Withdraw Money
    def withdraw_money(self,amount):
        if amount > self.balance:
            print("Insufficient Balance")
        elif amount <= 0 :
            print("Amount must be positive")
        else:
            self.balance-=amount
            print(f"{amount} deducted from the account")
    #Display Money
    def display_Balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")

def main():
    account = BankAccount("Alice", 1000)
    account.display_Balance()

    account.deposit_money(1506)
    account.withdraw_money(200)
    account.display_Balance()
    account.withdraw_money(2000) 
    account.display_Balance()


if __name__ == "__main__":
    main()