import datetime
import time

class Account:

    """Simple account class with accounts"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return utc_time



    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
        self._transaction_list=[(Account._current_time(), balance)]
        print("Accoount created for  " + self._name)

    def withdraw(self,amount):
        if 0<amount<=self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount should be greater than zero and less han the balance")
        self.show_balance()


    def deposit(self,amount):
        if amount>0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date,amount in self._transaction_list:
            if amount>0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{:7} {} on {}".format(amount,tran_type,date))


if __name__ == '__main__':
    tim = Account("Tim",2000)
    tim.deposit(5000000)
    time.sleep(5)
    tim.withdraw(200000)
    tim.show_transactions()

