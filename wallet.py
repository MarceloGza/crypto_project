from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5 
import binascii

import utility.hash_value as hv

PRIVATE_FILENAME = 'private_key.der'
PUBLIC_FILENAME = 'public_key.der'
class Wallet:
  
  def __init__(self):
    self.public_key = None
    self.private_key = None
    
  def create_keys(self): 
    try:
      with open(PRIVATE_FILENAME,'wb') as file:
        key = RSA.generate(2048, Random.new().read)
        private_key = key.export_key(format='DER')
        file.write(private_key)
        self.private_key = private_key
         
      
      with open(PUBLIC_FILENAME,'wb') as file:
        public_key = key.publickey().export_key(format='DER')
        file.write(public_key)
        self.public_key = public_key
      
    except IOError:
      print('Failed to create keys')
  
  def load_keys(self):
    try:
      with open(PRIVATE_FILENAME, 'rb') as file:
        self.private_key = file.read()
        
      with open(PUBLIC_FILENAME, 'rb') as file:
        self.public_key = file.read()
        
    except (IOError,IndexError):
      print('Failed to load keys')
  
  def sign_transaction(self, ord_dict):
    signer = PKCS1_v1_5.new(RSA.import_key(self.private_key))
    s_hash = hv.undigested_hash_ord_dict(ord_dict)
    signature = signer.sign(s_hash)
    return binascii.hexlify(signature).decode('ascii')
    
  def verify_signature(self):
    print('verifying')
          
  @property
  def public_id(self):
    if(self.public_key):
      return binascii.hexlify(self.public_key).decode('ascii')
    return None
  
    
  @property
  def private_id(self):
    if(self.private_key):
      return binascii.hexlify(self.private_key).decode('ascii')
    return None
    
# wallet = Wallet()

# print(wallet.public_id)
# wallet.create_keys()
# print(wallet.public_id)
