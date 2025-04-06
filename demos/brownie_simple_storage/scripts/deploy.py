import os
from ape import accounts, config, project, networks
from ape_accounts import import_account_from_private_key
from dotenv import load_dotenv

print("Script is running...")
with networks.ethereum.local.use_default_provider():
    faucet = accounts.test_accounts[0]
    my_account = accounts.load("test_account")
    faucet.transfer(my_account, "100 ether")


def deploy_simple_storage():
    # NOTE: THis is the code to create the account based on the settings on config.yaml and get Private key in .env
    # load_dotenv()
    # wallets = config.get_config("wallets")
    # alias = wallets["alias"]
    # passphrase = wallets["passphrase"]
    # private_key = os.getenv("PRIVATE_KEY")
    # account = import_account_from_private_key(alias, passphrase, private_key)

    account = get_account()
    simple_storage = project.SimpleStorage.deploy(sender=account)
    print("run 1")
    stored_value = simple_storage.retrieve(sender=account)
    print(stored_value)
    print("run 2")
    transaction = simple_storage.store(15, sender=account)
    print("run 3")
    updated_stored_value = simple_storage.retrieve(sender=account)
    print("Updated", updated_stored_value)


def get_account():
    chain_id = networks.active_provider.network.chain_id
    print("networkkkkkkkkkkkkkkkkkk", chain_id)
    if chain_id == 1337:
        account = accounts.load("test_account")
    elif chain_id == 11155111:
        account = accounts.load("my_account")

    print("accounttttttttttttttt", account)
    return account


def main():
    deploy_simple_storage()
