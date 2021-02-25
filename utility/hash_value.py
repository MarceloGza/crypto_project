import hashlib as hl 

def hash_value(*data):
  hash_string=''
  
  for value in data:
    hash_string = hash_string + str(value)
  # print(hash_string)
  return hl.sha256(hash_string.encode()).hexdigest()
 
def hash_ord_dict(ordered_dict):
  return hash_value(*[ordered_dict[key] for key in ordered_dict])