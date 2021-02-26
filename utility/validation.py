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
  
  @classmethod
  def get_proof_of_work(self):
    print(1)
    
  @classmethod
  def validate_proof_of_work(self):
    print(1)
    
  