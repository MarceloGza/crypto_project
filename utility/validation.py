from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from copy import deepcopy
import utility.hash_value as hv


class Validation():
  
  @classmethod
  def validate_c_transactions(self, c_transactions):
    return all([self.validate_signature(transaction) for transaction in c_transactions])
  
  @classmethod
  def validate_chain(self, chain):
    for (index,block) in enumerate(chain):
      if index != 0:
        if (not self.validate_proof_of_work(block)) or (block['prev_hash'] != hv.hash_ord_dict(chain[index-1])): 
          return False   
    return True
  
  @staticmethod
  def validate_signature(transaction):
    copy_transaction = deepcopy(transaction)
    signature = hv.hex_to_bin(copy_transaction.pop('signature'))
    public_key = RSA.import_key(hv.hex_to_bin(copy_transaction['sender']))
    verifier = PKCS1_v1_5.new(public_key)
    v_hash = hv.undigested_hash_ord_dict(copy_transaction)
    return verifier.verify(v_hash,signature)
    
  @classmethod
  def validate_proof_of_work(self, block):
    copy_block = deepcopy(block)
    return self.meets_proof_condition(copy_block['prev_hash'], copy_block['transactions'][:-1], copy_block['proof'])
  
  @classmethod
  def generate_proof_of_work(self, previous_hash, transactions_to_add):
    new_proof = 0
    while not self.meets_proof_condition(previous_hash,transactions_to_add,new_proof):
        new_proof += 1
    return new_proof
  
  @staticmethod  
  def meets_proof_condition(prev_hash, transaction, proof):
    amount_of_zeros = 2
    condition = amount_of_zeros*'0'
    return hv.hash_value(prev_hash, transaction, proof).startswith(condition)
    