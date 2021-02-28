import utility.save_load_bin as slb 
import utility.hash_value as hv 

from copy import deepcopy

from block import Block
from wallet import Wallet
from transaction import Transaction
from utility.validation import Validation


GENESIS_BLOCK = Block(0,'', [], 0)
CHAIN_FILENAME = 'chain'
C_TRAN_FILENAME = 'c_transactions'

class Blockchain:
  
  def __init__(self):
    self.wallet = Wallet()
    self.id = None
    self.balance = 0
    self.chain = self.load_chain()
    self.current_transactions = self.load_current_transactions()
    
  def load_chain(self):
    try:
      loaded_chain = slb.load_file(CHAIN_FILENAME)
      if Validation.validate_chain(loaded_chain):
        return loaded_chain
      print('Invalid chain detected')
      raise IOError
    except (IOError,IndexError):
      return [GENESIS_BLOCK.dictionary()]
      
  def load_current_transactions(self):
    try:
      loaded_c_transactions = slb.load_file(C_TRAN_FILENAME)
      if Validation.validate_c_transactions(loaded_c_transactions):
        return loaded_c_transactions
      print('Invalid current transactions detected')
      raise IOError
    except (IOError, IndexError):
      return []
  
  def save_chain(self):
    try:
      if Validation.validate_chain(self.chain):
        slb.save_file(CHAIN_FILENAME, self.chain)
      else:
        print('Unable to save invalid blockchain')
    except IOError:
      print('Unable to save blockchain')
  
  def save_c_transactions(self):
    try:
      if Validation.validate_c_transactions(self.current_transactions):
        slb.save_file(C_TRAN_FILENAME, self.current_transactions)
      else:
        print('Unable to save invalid current transactions')
    except IOError:
      print('Unable to save blockchain')
  
  def initialize_wallet(self,method):
    if method == 'CREATE':
      self.wallet.create_keys()
    elif method == 'LOAD':
      self.wallet.load_keys()
    else:
      raise ValueError('Invalid method to initialize wallet') 
    self.id = self.wallet.public_id
    
  
  def get_balance(self, public_id):
    if Validation.validate_chain(self.chain) and Validation.validate_c_transactions(self.current_transactions):
      chain_movements = [ (-transaction['amount'] if transaction['sender']== public_id 
                           else transaction['amount'] if transaction['recipient']== public_id else 0) 
                        for block in self.chain for transaction in block['transactions']]
      
      c_transactions_movements = [ (-transaction['amount'] if transaction['sender']== public_id 
                                    else 0) for transaction in self.current_transactions]
      return sum(chain_movements) + sum(c_transactions_movements)
    
    return 0   
  
  def add_transaction(self, recipient, amount):
    
    if not self.id:
      print('Public & Private Keys required to make transactions')
      return
    
    balance = self.get_balance(self.id)
    
    if balance < amount:
      print('Insufficient funds for transaction')
      return
      
    copy_c_transactions = self.current_transactions
    
    new_transaction = Transaction(self.id, recipient, amount)
    new_transaction.signature = self.wallet.sign_transaction(new_transaction.dictionary())
    
    copy_c_transactions.append(new_transaction.dictionary())
    
    self.current_transactions = copy_c_transactions
    self.save_c_transactions()
  
  def mine(self):
    if not self.id:
      print('Public Key required to mine')
      
    current_index = len(self.chain)
    previous_block = self.chain[-1]
    previous_hash = hv.hash_ord_dict(previous_block)
    transactions_to_add = self.current_transactions
    
    if not Validation.validate_c_transactions(transactions_to_add):
      return
    
    proof = Validation.generate_proof_of_work(previous_hash, transactions_to_add)
    
    mining_reward = Transaction('MINING', self.id, 10)
    transactions_to_add.append(mining_reward.dictionary())
    
    new_block = Block(current_index, previous_hash, transactions_to_add, proof)
    
    copy_chain = self.chain
    copy_chain.append(new_block.dictionary())
    
    if not Validation.validate_chain(copy_chain):
      return
    
    self.current_transactions = []
    self.chain = copy_chain
    
    self.save_c_transactions()
    self.save_chain()
    
  @property
  def chain(self):
    return deepcopy(self.__chain)
  
  @chain.setter
  def chain(self, new_chain):
    if Validation.validate_chain(new_chain):
      self.__chain = new_chain
    
  @property
  def current_transactions(self):
    return deepcopy(self.__current_transactions)
  
  @current_transactions.setter
  def current_transactions(self, new_c_transactions):
    if Validation.validate_c_transactions(new_c_transactions):
      self.__current_transactions = new_c_transactions
      