"""
Create a Bill class which has a final amount attribute.
    - create a behaviour where we can add item with amount
    - all the items added should be stored with amount at Bill class
    - final amount should be summation of all the individual item amount
"""

class Bill:
    """
    Bill class
    """
    total_bills: int = 0

    def __init__(self):
        self.final_amount = 0
        self.items = {}
        Bill.total_bills += 1

    def add_item(self, item: str, amount: int):
        self.items[item] = amount
        self.final_amount += amount

    def __add__(self, other):
        return self.final_amount + other.final_amount

    def __str__(self):
        return "Bill Class"

    def __repr__(self):
        return "Bill()"
b1 = Bill()

b2: Bill = Bill()

print(b1)
# b1.add_item('doas', 70)
# b1.add_item('tea', 20)
#
# # print(b1.final_amount)
# # print(b1.items)
# # print(b1.total_bills)
#
# print(b1.__dict__)
# print("---------------------------")
# print(Bill.total_bills)
# print(Bill.__dict__)

# b2 = Bill()
# b2.add_item('Idli', 40)
#
#
#
# print(b2.final_amount)
# print(b2.items)
# print(b2.total_bills)
#
# print(b1 + b2)