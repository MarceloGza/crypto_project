import utility.save_load_bin as slb 
import utility.hash_value as hv 

from copy import deepcopy
from copy import copy

from block import Block
from wallet import Wallet
from transaction import Transaction

GENESIS_BLOCK = Block(0,'', [], 0).dictionary()
CHAIN_FILENAME = 'chain'
C_TRAN_FILENAME = 'c_transactions'

class Blockchain:
  
  def __init__(self):
    self.id = None
    self.chain = self.load_chain()
    self.current_transactions = self.load_current_transactions()
    
  def load_chain(self):
    try:
      return slb.load_file(CHAIN_FILENAME)
    except (IOError,IndexError):
      return [GENESIS_BLOCK]
      
  def load_current_transactions(self):
    try:
      return slb.load_file(C_TRAN_FILENAME)
    except (IOError, IndexError):
      return []
  
  def save_chain(self):
    try:
      slb.save_file(CHAIN_FILENAME, self.chain)
    except IOError:
      print('Unable to save blockchain')
  
  def save_c_transactions(self):
    try:
      slb.save_file(C_TRAN_FILENAME, self.current_transactions)
    except IOError:
      print('Unable to save blockchain')
      
  def add_transaction(self, sender, recipient, amount):
    new_transaction = Transaction(sender, recipient, amount).dictionary()
    copy_c_transactions = self.current_transactions
    copy_c_transactions.append(new_transaction)
    self.current_transactions = copy_c_transactions
    self.save_c_transactions()
  
  def mine(self):
    current_index = len(self.chain)
    previous_block = self.chain[-1]
    previous_hash = hv.hash_ord_dict(previous_block)
    proof = 1
    new_block = Block(current_index, previous_hash, self.current_transactions, proof).dictionary()
    copy_chain = self.chain
    copy_chain.append(new_block)
    self.chain = copy_chain
    self.save_chain()
    
  @property
  def chain(self):
    return deepcopy(self.__chain)
  
  @chain.setter
  def chain(self, new_chain):
    self.__chain = new_chain
    
  @property
  def current_transactions(self):
    return deepcopy(self.__current_transactions)
  
  @current_transactions.setter
  def current_transactions(self, new_c_transactions)
    self.__current_transactions = new_c_transactions
      
  
blockchain = Blockchain()

blockchain.add_transaction('marcelo','me',5)
blockchain.mine()

print(blockchain.current_transactions)
print(blockchain.chain)