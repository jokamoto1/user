class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name + "'s balance: " +str(self.balance))
        return self
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self
bob = User("Bobby", "bob@email")
bob.make_deposit(1000).make_deposit(20).make_deposit(30).make_withdrawl(50).display_user_balance()
"""bob.make_deposit(1000)
bob.make_deposit(20)
bob.make_deposit(30)
bob.make_withdrawl(50)
bob.display_user_balance()"""
joe = User("Joey", "joe@email")
joe.make_deposit(2000).make_deposit(40).make_withdrawl(574).make_withdrawl(40).display_user_balance()
"""joe.make_deposit(2000)
joe.make_deposit(40)
joe.make_withdrawl(574)
joe.make_withdrawl(40)
joe.display_user_balance()"""
jeremy = User("Jeremy", "jeremy@email")
jeremy.make_deposit(10000).make_withdrawl(400).make_withdrawl(4000).make_withdrawl(300).display_user_balance()
bob.transfer_money(jeremy, 1000000).display_user_balance()
jeremy.display_user_balance()
"""jeremy.make_deposit(10000)
jeremy.make_withdrawl(400)
jeremy.make_withdrawl(4000)
jeremy.make_withdrawl(300)
jeremy.display_user_balance()
bob.transfer_money(jeremy, 1000000)
bob.display_user_balance()
jeremy.display_user_balance()"""