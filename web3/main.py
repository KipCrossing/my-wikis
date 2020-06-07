from web3 import Web3
import os
from eth_account import Account
import pprint



private_key = os.getenv('PRIVATE_KEY')
acct = Account.from_key(private_key)

TOKEN = os.environ['INFURA_API_KEY']

infura_url = "https://ropsten.infura.io/v3/"+ TOKEN

print(infura_url)

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)
print("Gas Price: ",web3.fromWei(web3.eth.gasPrice, "ether")*1000)
print(web3.eth.accounts)
print(web3.eth.hashrate)
# Public key

print("Private key: " + acct.privateKey.hex())
print("Address: " + acct.address)

balance = web3.eth.getBalance(acct.address)

print(web3.fromWei(balance, "ether")*1000)

print((7000/0.000003)/1000)

# pprint.pprint(dict(web3.eth.getBlock('latest')))