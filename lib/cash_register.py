#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, item, price, quantity=0):
    if quantity > 0:
      all_items = price * quantity
      self.last_transaction = all_items
      while quantity > 0:
        self.items.append(item)
        quantity -= 1
      self._total += all_items
    else:
      self.items.append(item)
      self._total += price
      self.last_transaction = price
    return self._total
  
  def apply_discount(self):
    if self.discount > 0:
      self._total -= (self.discount *10000) / self._total
      print(f"After the discount, the total comes to ${int(self._total)}.")
      return self._total
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.items.pop(-1)
    self.total -= self.last_transaction
  
  def get_total(self):
    return self._total
  
  def set_total(self, total):
    self._total = total
  
  total = property(get_total, set_total)