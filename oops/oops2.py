class Account():
  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount
    print(f"Balance after deposit => {self.balance}")

  def withdraw(self,amount):
    if(amount > self.balance):
      print(f"Withdraw amount -> {amount} Failed")
      print("Balance Insufficient to withdraw")
      print(f"Balance - {self.balance}")
    else:
      self.balance -= amount
      print(f"Balance after withdraw => {self.balance}")


acct1 = Account('Jose',100)

print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)


acct1.withdraw(75)


acct1.withdraw(500)


