from abc import ABC, abstractmethod

class BaseBill(ABC):

    @abstractmethod
    def add_item(self, item: str, amount: float):
        pass

    @abstractmethod
    def remove_item(self):
        pass


class Bill(BaseBill):
    BILL_COUNT = 0

    def __init__(self):
        self.items = {}
        Bill.BILL_COUNT += 1
        self.__amount = 0.0

    def add_item(self, item, amount):
        self.items[item] = amount
        self.__amount = self.amount + amount

    def remove_item(self):
        pass

    @property
    def amount(self):
        return self.__amount

b1 = Bill()
b1.add_item('Dosa', 70)
b1.add_item('Idli', 90)

print(b1.items)
print(b1.BILL_COUNT)
print(b1.amount)
print(b1.amount)