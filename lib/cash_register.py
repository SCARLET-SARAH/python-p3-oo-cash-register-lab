#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)

    def apply_discount(self):
      if self.discount > 0:
        discounted_total = self.total * (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${discounted_total:.2f}.")
        self.total = discounted_total
      else:
        print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= self.get_item_price(last_item)
            if not self.items:
                self.total = 0
        else:
            print("There is no item to void.\n")

    def get_item_price(self, item):
        for item_dict in self.items:
            if item_dict["item"] == item:
                return item_dict["price"]
        return 0

    def get_items(self):
        return self.items

