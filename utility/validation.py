from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from copy import deepcopy
import utility.hash_value as hv
import binascii

class Validation():
  
  @staticmethod
  def validate_chain(chain):
    for (index,block) in enumerate(chain):
      if index != 0:
        previous_hash = hv.hash_ord_dict(chain[index-1])
        if block['prev_hash'] != previous_hash: 
          return False   
    return True
  
  @classmethod
  def validate_signature(self,transaction):
    copy_transaction = deepcopy(transaction)
    signature = self.hex_to_bin(copy_transaction.pop('signature'))
    public_key = RSA.import_key(self.hex_to_bin(copy_transaction['sender']))
    verifier = PKCS1_v1_5.new(public_key)
    v_hash = hv.undigested_hash_ord_dict(copy_transaction)
    return verifier.verify(v_hash,signature)
    
  @staticmethod
  def hex_to_bin(hash_hex):
    return binascii.unhexlify(hash_hex)
    
  
  @classmethod
  def get_proof_of_work(self):
    print(1)
    
  @classmethod
  def validate_proof_of_work(self):
    print(1)
    
  