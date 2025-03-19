from ape import accounts
print("Script is running...")


def deploy_simple_storage():
    account = accounts.load("myaccount")
    print(account)


def main():
    deploy_simple_storage()
