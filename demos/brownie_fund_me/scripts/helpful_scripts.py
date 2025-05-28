from ape import project, accounts, networks
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIROMENT = ["development"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    chain_id = networks.active_provider.network.chain_id
    if chain_id == 1337:
        account = accounts.load("test_account")
    elif chain_id == 11155111:
        account = accounts.load("my_account")

    return account


def deploy_mocks(account):
    print("Deploying mocks...")

    # Try to get the last deployed instance
    try:
        aggregator = project.MockV3Aggregator[-1]
    except IndexError:
        # If not deployed, deploy a new one
        aggregator = project.MockV3Aggregator.deploy(
            DECIMALS, Web3.to_wei(STARTING_PRICE, "ether"), sender=account
        )
    print(f"Mock deployed at: {aggregator.address}")
    return aggregator


def main(): ...
