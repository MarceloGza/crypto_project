from collections import OrderedDict
import utility.hash_value as hv

class Block:
  
  def __init__(self, index, prev_hash, transactions, proof):
    self.index = index 
    self.prev_hash = prev_hash
    self.transactions = transactions
    self.proof = proof
    
  def __repr__(self):
    return str(self.dictionary())
  
  def dictionary(self):
    return OrderedDict([('index', self.index), ('prev_hash', self.prev_hash), ('transactions', self.transactions), ('proof', self.proof)])
  
  
  