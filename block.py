from collections import OrderedDict
import utility.hash_value as hv

class Block:
  
  def __init__(self, index, prev_hash, transactions):
    self.index = index 
    self.prev_hash = prev_hash
    self.transactions = transactions
    self.proof = 0
    
  def __repr__(self):
    return str(self.dictionary())
  
  def dictionary(self):
    return OrderedDict([('index', self.index), ('prev_hash', self.prev_hash), ('transactions', self.transactions), ('proof', self.proof)])
  
  def generate_proof_of_work(self):
    has_valid_proof = False
    new_proof = 0
    while not has_valid_proof:
      if hv.hash_value(self.prev_hash, self.transactions, new_proof).startswith('00'):
        has_valid_proof = True
      else:
        new_proof = new_proof + 1
    self.proof = new_proof
  
  