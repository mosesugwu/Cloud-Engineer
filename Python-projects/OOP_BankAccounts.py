# Class: BankAccount (Blueprint for a bank account)
class BankAccount:
    # Attributes: account_number, account_holder, balance
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Method: deposit (Add money to the account)
    def deposit(self, amount):
        self.balance += amount

    # Method: withdraw(Take money from the account)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawl Successful.")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient funds!") 
    # Method: display_account_info (Display account information)
    def display_account_info(self):
        print("Account Number:", self.account_number) 
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

# Class: SavingsAccount (Special type of account with interest)
class SavingsAccount(BankAccount):
    # Attributes: interest_rate
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate 

    # Method: calculate_interest (calculate and add the interest to the account)
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


# Function to validate the account number

# Encapsulation: A seperate function outside the class to check the validity of the account number.
def validate_account_number(account_number):
    if len(account_number) != 10:
        return False
    return True


# Create an instance of the SavingsAccount class

# Object: savings_account (An actual savings account with specific details)
valid_account_number = False
while not valid_account_number:
    account_number = input("Enter account number(10 digits): ")
    valid_account_number = validate_account_number(account_number) 
    if not valid_account_number:
        print("Invalid account number. Please enter a 10-digit number.")


account_holder = "John Bruno."
balance = 650000
interest_rate = 0.15
savings_account = SavingsAccount(account_number, account_holder, balance, interest_rate) 

# Display initial account information

# Ploymorphism: Treating savings_account as a BankAccount object to display its information.
print("\nAccount Information:") 
savings_account.display_account_info()

# Withdrawal process

# Polymorphism: Treating savings_account as a BankAccount object to perform a withdrawal.
print("\nWithdrawal Process:") 
withdrawal_amount = float(input("Enter the withdrawal amount: ")) 
while withdrawal_amount > savings_account.balance:
    print("Withdrawal amount exceeds the account balance.")
    withdrawal_amount = float(input("Enter a valid withdrawal amount:")) 

savings_account.withdraw(withdrawal_amount) 

# Calculate interest and display final account information

# Ploymorphism: Treating a savings_account as a SavingsAccount object to calculate interest.
print("\nCalculating interest....")
savings_account.calculate_interest()
print("\nFinal Accounts Information:") 
savings_account.display_account_info()





