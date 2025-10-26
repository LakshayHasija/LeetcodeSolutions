class Bank:

    def __init__(self, balance: List[int]):
        self.acc_bal=[]
        for i in balance:
            self.acc_bal.append(i)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<1 or account1>len(self.acc_bal) or account2<1 or account2>len(self.acc_bal):
            return False
        if self.acc_bal[account1-1]<money:
            return False
        self.acc_bal[account1-1]-=money
        self.acc_bal[account2-1]+=money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account<1 or account>len(self.acc_bal):
            return False
        self.acc_bal[account-1]+=money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account<1 or account>len(self.acc_bal):
            return False
        if self.acc_bal[account-1]<money:
            return False
        self.acc_bal[account-1]-=money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)