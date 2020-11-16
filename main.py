class Value:
    def __set__(self, object, value):
        self.value = int(value * (1 - object.commission))

    def __get__(self, object, object_t):
        return self.value


class Account:
    amount = Value()
    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)