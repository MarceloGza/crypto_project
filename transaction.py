from datetime import datetime
from collections import OrderedDict

class Transaction:
  
  def __init__(self, sender, recipient, amount):
    self.sender = sender
    self.recipient = recipient
    self.amount = amount
    self.time = str(datetime.now())
    self.signature = None
    
  def __repr__(self):
    return self.dictionary()
    
  def dictionary(self):
    if not self.signature:
      return OrderedDict([('sender', self.sender),('recipient', self.recipient), ('amount', self.amount), ('time', self.time)])
    return OrderedDict([('sender', self.sender),('recipient', self.recipient), ('amount', self.amount), ('time', self.time), ('signature', self.signature)])
  
