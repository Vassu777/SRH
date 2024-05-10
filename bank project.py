class BanckAccount():
    
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
    
    def diposite(self,amount):
        self.balance += amount
        print(f"your deposited balence is{amount} and your balance is {self.balance}")
    
    def withdrawal(self,amount):
        if self.balance >= amount:
           self.balance -= amount
           print(f"your withdrawl amount is {amount} and your blance is {self.balance}")
        else:
            print('insuficiant funds. please try again later.')

    def check_balance(self):
        print(f"current balence of {self.name} is {self.balance}")

def main():
    print("welcome to the bank.")

    name  = input("enter your name : ")
    initialize_balance = float(input("enter your initial balance"))
    account = BanckAccount(name,initialize_balance)

    while True:
        print("\n1.deposite ")
        print("2.withdraw")
        print("3.check_balance")
        print("4.exit")

        choice = input("enter your choice.")
        
        if choice == '1':
            amount = float(input("enter the diposite amount :"))
            account.diposite(amount)
        
        elif choice == '2':
            amount = float(input("enter the withdraw amount :"))
            account.withdrawal(amount)
        
        elif choice == '3':
            account.check_balance()
            
        
        else:
            print("invalid input !")

main()


'JHSJHLFHAJHFKJ'
<<<<<<< HEAD
kdjlkdjf
;ljflkhdfjet
=======


>>>>>>> d083d8c64b7c844037d72d51750967e2b25e8a14
