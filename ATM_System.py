class Customer:
    def __init__(self, name, pin, account_number):
        self.name = name
        self.pin = pin
        self.account_number = account_number

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.balance

class BankServer:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account_number, balance):
        account = BankAccount(account_number, balance)
        self.accounts[account_number] = account
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

class ATM:
    def __init__(self, bank_server):
        self.bank_server = bank_server
    
    def authenticate(self, customer):
        account = self.bank_server.get_account(customer.account_number)
        if account and customer.pin == "1234":  # Simplified: assuming PIN is always "1234"
            return account
        else:
            print("Authentication failed.")
            return None
    
    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
    
    def withdraw(self, account):
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    
    def deposit(self, account):
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    
    def main(self):
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        account_number = input("Enter your account number: ")

        customer = Customer(name, pin, account_number)
        
        # Authenticate the customer
        account = self.authenticate(customer)
        if not account:
            return  # Exit if authentication fails
        
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                print(f"Your balance is: {account.get_balance()}")
            elif choice == '2':
                self.withdraw(account)
            elif choice == '3':
                self.deposit(account)
            elif choice == '4':
                print("Exiting the ATM system.")
                break
            else:
                print("Invalid choice. Please try again.")

# Main Program
if __name__ == "__main__":
    # Initialize BankServer and add an account with initial balance
    bank_server = BankServer()
    bank_server.add_account("12345678", 10000)  # Account number and initial balance

    # Initialize ATM and start the system
    atm = ATM(bank_server)
    atm.main()
