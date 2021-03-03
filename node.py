from flask import Flask, request, send_from_directory, render_template, jsonify
from flask_cors import CORS
import os
import json

from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

CORS(app)

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))


@app.route('/', methods=['GET'])
def get_ui():
  return render_template('node.html', last_updated=dir_last_updated('./static'))

@app.route('/wallet', methods=['POST'])
def create_keys():
  result = blockchain.initialize_wallet('CREATE')
  if result == 'Success':
    response = {
      'message': 'Wallet created successfully',
      'public_key': blockchain.id,
      'private_key': blockchain.wallet.private_id,
      'balance': blockchain.get_balance(blockchain.id)
    }
  elif result == 'Failure':
    response = {
      'message': 'Failed to create Wallet'
    }
  elif result == 'Invalid':
    response = {
      'message': 'Invalid attempt to initialize Wallet'
    }
  else:
    response = {
      'message': 'Unexpected error while creating Wallet'
    }
  return response

@app.route('/wallet', methods=['GET'])
def load_keys():
  result = blockchain.initialize_wallet('LOAD')
  if result == 'Success':
    response = {
      'message': 'Wallet loaded successfully',
      'public_key': blockchain.id,
      'private_key': blockchain.wallet.private_id,
      'balance': blockchain.get_balance(blockchain.id)
    }
  elif result == 'Failure':
    response = {
      'message': 'Failed to create Wallet'
    }
  elif result == 'Invalid':
    response = {
      'message': 'Invalid attempt to initialize Wallet'
    }
  else:
    response = {
      'message': 'Unexpected error while creating Wallet'
    }
  return response

@app.route('/add-transaction', methods=['POST'])
def add_transaction():
  pass

@app.route('/chain', methods=['GET'])
def get_blockchain():
  response = {
    'message': 'Blockchain loaded successfully', 
    'blockchain': blockchain.chain
  }
  return response

if __name__ == '__main__':
  app.run('127.0.0.1', 5000)