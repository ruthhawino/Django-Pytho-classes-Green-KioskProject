class Account:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        balance = 0
        for transaction in self.deposits:
            balance += transaction["amount"]
        for transaction in self.withdrawals:
            balance -= transaction["amount"]
        balance -= self.loan_balance
        return balance

    def deposit(self, amount):
        transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = {"amount": amount, "narration": "withdrawal"}
        self.withdrawals.append(transaction)

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print("Loan approved!")
            else:
                print("Loan amount exceeds maximum limit.")
        else:
            print("Loan request denied.")
        
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.deposit(amount - self.loan_balance)
            self.loan_balance = 0
        else:
            self.withdrawal(amount)
            self.loan_balance -= amount

    def transfer(self, amount, destination_account):
        balance = self.check_balance()
        if amount <= balance:
            self.withdrawal(amount)
            destination_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient funds for transfer.")
account1 = Account()
account1.deposit(1000)
account1.withdrawal(500)
account1.print_statement()
account1.borrow_loan(5000)
account1.repay_loan(2000)
account2 = Account()
account1.transfer(500, account2)
