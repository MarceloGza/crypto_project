import pickle

def save_file(filename, data):
  with open(filename + '.bin', 'wb') as file:
    file.write(pickle.dumps(data))
    
def load_file(filename):
  with open(filename + '.bin', 'rb') as file:
    return pickle.loads(file.read())

