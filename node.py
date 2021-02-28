from blockchain import Blockchain

blockchain = Blockchain()

blockchain.initialize_wallet('LOAD')

blockchain.add_transaction('asd', 5)
blockchain.add_transaction('asdasd', 10)

blockchain.mine()

blockchain.add_transaction('asdasd', 10)

print(blockchain.get_balance(blockchain.id))
print(blockchain.get_balance('asdasd'))
print(blockchain.get_balance('asd'))

print(blockchain.chain)
print(blockchain.current_transactions)
