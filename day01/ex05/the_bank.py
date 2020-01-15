
class Account(name):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1
    def transfer(self, amount):
        self.value += amount
	def transfer_neg(self, amount):
		self.value -= amout

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    def add(self, account):
        self.account.append(account)
    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
			"""
			# check on dest
			if amount < 0:
				return False
			for id, name in enumerate(self.account, 1):
				if origin == id or origin == name:
					if (self.account[id].value < amount)
						return False
			for id, name in enumerate(self.acount, 1)
				if dest == id or dest == name:

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
"""

bank = Bank()
richard = Account("richard")
richard.value = 500
henri = Account("Henri")
henri.value = 250
bank.add(richard)
bank.add(henri)
bank.add(Account("michel"))
