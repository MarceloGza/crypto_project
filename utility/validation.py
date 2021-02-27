from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from copy import deepcopy
import utility.hash_value as hv


class Validation():
  
  @staticmethod
  def validate_chain(chain):
    for (index,block) in enumerate(chain):
      if index != 0:
        previous_hash = hv.hash_ord_dict(chain[index-1])
        if block['prev_hash'] != previous_hash: 
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
    
  @staticmethod
  def validate_proof_of_work(block):
    copy_block = deepcopy(block)
    return hv.hash_value(copy_block['prev_hash'], copy_block['transactions'], copy_block['proof']).startswith('00')
    