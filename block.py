from collections import OrderedDict

class Block:
  
  def __init__(self, index, prev_hash, transactions, proof):
    self.index = index 
    self.prev_hash = prev_hash
    self.transactions = transactions
    self.proof = proof
    
  def __repr__(self):
    return self.dictionary()
  
  def dictionary(self):
    return OrderedDict([('index', self.index), ('prev_hash', self.prev_hash), ('transactions', self.transactions), ('proof', self.proof)])
  
# block = Block(0,'qerqrqerqr',[{'key':'value','key2':5},{'key':'value','key2':5}],356)

# a = block.hashed()

# print(a)


  