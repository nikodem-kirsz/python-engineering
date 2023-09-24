import unittest

class TradeLedger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TradeLedger, cls).__new__(cls)
        return cls._instance
        
    def __init__(self) -> None:
        self._accounts: Account = {}
        self.account_counter = 0

    def create_account(self, name, balance = 0):
        self.account_counter += 1
        new_account = Account(self.account_counter, name, balance)
        print(new_account)
        self._accounts[self.account_counter] = new_account
        print(new_account._account_id)
        return new_account
    
    def delete_account(self, account_id):
        account = self._accounts.pop(account_id, None)
        return account
    
    def transfer_cash(self, from_account_id, to_account_id, amount):
        from_acc = self._accounts.get(from_account_id)
        to_acc = self._accounts.get(to_account_id)

        if from_acc and to_acc:
            from_acc.widthdraw(amount)
            to_acc.transfer(amount)

    @property    
    def get_accounts(self):
        return self._accounts

class Account:
    def __init__(self, account_id, name, balance) -> None:
        self._account_id = account_id
        self._name = name
        self.balance = balance
    
    @property
    def check_balance(self):
        return self.balance

    def widthdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount):
        self.balance += amount

    @property
    def account_name(self):
        return self._name

    @property
    def account_id(self):
        return self._account_id

class TestTradeLedger(unittest.TestCase):
    def test_trade_ledger(self):
        trade_ledger = TradeLedger()
        acc1 = trade_ledger.create_account("Niko", 1000)
        acc2 = trade_ledger.create_account("Marta", 2000)

        # Ensure unique account IDs are generated
        self.assertNotEqual(acc1.account_id, acc2.account_id)

        self.assertEqual(acc1.check_balance, 1000)
        self.assertEqual(acc2.check_balance, 2000)
        trade_ledger.transfer_cash(acc1.account_id, acc2.account_id, 500)
        self.assertEqual(acc1.check_balance, 500)
        self.assertEqual(acc2.check_balance, 2500)


if __name__ == "__main__":
    unittest.main()