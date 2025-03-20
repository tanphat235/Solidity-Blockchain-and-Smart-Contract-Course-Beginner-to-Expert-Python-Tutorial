import os
from ape import accounts, config, project
from ape_accounts import import_account_from_private_key
from dotenv import load_dotenv

print("Script is running...")


def deploy_simple_storage():
    # NOTE: THis is the code to create the account based on the settings on config.yaml and get Private key in .env
    # load_dotenv()
    # wallets = config.get_config("wallets")
    # alias = wallets["alias"]
    # passphrase = wallets["passphrase"]
    # private_key = os.getenv("PRIVATE_KEY")
    # account = import_account_from_private_key(alias, passphrase, private_key)

    account = accounts[0]
    account.set_autosign(True)
    simple_storage = project.SimpleStorage.deploy(sender=account)
    print("run 1")
    stored_value = simple_storage.retrieve(sender=account)
    print(stored_value)
    print("run 2")
    transaction = simple_storage.store(15, sender=account)
    print("run 3")
    updated_stored_value = simple_storage.retrieve(sender=account)
    print("Updated", updated_stored_value)


def main():
    deploy_simple_storage()
