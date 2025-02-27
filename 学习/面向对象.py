class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存款 {amount} 元成功，当前余额: {self.balance} 元。")
        else:
            print("存款金额必须大于 0。")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"取款 {amount} 元成功，当前余额: {self.balance} 元。")
        else:
            print("取款失败，余额不足或取款金额无效。")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, annual_interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.annual_interest_rate = annual_interest_rate

    def add_interest(self):
        interest = self.balance * self.annual_interest_rate
        self.balance += interest
        print(f"已添加利息 {interest} 元，当前余额: {self.balance} 元。")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"取款 {amount} 元成功，当前余额: {self.balance} 元。")
        else:
            print("取款失败，超过透支限额或取款金额无效。")


# 测试代码
savings = SavingsAccount("123456", "张三", 1000)
savings.deposit(500)
savings.add_interest()

checking = CheckingAccount("654321", "李四", 200, 500)
checking.withdraw(300)
checking.withdraw(400)