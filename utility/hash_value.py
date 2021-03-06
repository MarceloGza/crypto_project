import hashlib as hl
from Crypto.Hash import SHA256
import binascii

def hash_value(*data):
  hash_string=''
  
  for value in data:
    hash_string = hash_string + str(value)
  return hl.sha256(hash_string.encode()).hexdigest()
 
def hash_ord_dict(ordered_dict):
  return hash_value(*[value for key,value in ordered_dict.items()])

def undigested_hash_ord_dict(ordered_dict):
  hash_string=''
  for val in [value for key,value in ordered_dict.items()]:
    hash_string = hash_string + str(val)
  return SHA256.new(hash_string.encode())

def hex_to_bin(hash_hex):
  return binascii.unhexlify(hash_hex)