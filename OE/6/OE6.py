class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__display_balance()
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__display_balance()
        else:
            print("Invalid withdrawal amount. Amount must be positive and less than or equal to the balance.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance must be a non-negative number.")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")

account = BankAccount("123456789", 1000.0)
account.display_account_info()
account.deposit(500.0)
account.withdraw(200.0)
account.set_balance(1500.0)
account.set_balance(-50.0)
account.display_account_info()