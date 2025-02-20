import json
from solcx import compile_standard
from web3 import Web3

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
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chainid = 1337
my_address = "0x309dcB0a038CBA11d5Edd4D274cD0EAff5962485"
private_key = "0xb45c06afd1b599dcbee8dbe134286b3d09ead237dcb4fb326ba851a9e0155622"

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)
