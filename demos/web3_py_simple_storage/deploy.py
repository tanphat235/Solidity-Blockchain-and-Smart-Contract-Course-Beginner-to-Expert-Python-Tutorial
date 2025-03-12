import json
import os
from solcx import compile_standard
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:  # Read file .sol to deploy
    simple_storage_file = file.read()


# Compole our Solidity

compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0"
)

with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file)

# get bytecode
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))
chainid = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the lasttest transaction
nonce = w3.eth.get_transaction_count(my_address)
# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = SimpleStorage.constructor().build_transaction(
    {"chainId": chainid, "from": my_address, "nonce": nonce})
signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
store_transaction = simple_storage.functions.store(15).build_transaction({
    "chainId": chainid, "from": my_address, "nonce": nonce + 1})
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key)
send_store_txn = w3.eth.send_raw_transaction(
    signed_store_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(simple_storage.functions.retrieve().call())
