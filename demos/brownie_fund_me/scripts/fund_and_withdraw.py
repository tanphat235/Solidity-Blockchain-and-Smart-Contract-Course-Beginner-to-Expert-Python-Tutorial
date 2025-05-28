import time
from web3 import Web3
from ape import project, accounts, networks, chain
from scripts.helpful_scripts import get_account

print(f"Active Network: {networks.active_provider.network.name}")
print(chain.contracts.get_deployments(project.FundMe))
fund_me = chain.contracts.get_deployments(project.FundMe)[-1]
account = get_account()


def fund():
    time.sleep(5)
    entrance_fee = fund_me.getEntranceFee(sender=account)
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    buffer = Web3.to_wei(0.0001, "ether")
    fund_me.fund(value=entrance_fee + buffer, sender=account)


def withdraw():
    print(f"owner {fund_me.owner}")
    print(f"balance {fund_me.balance}")
    value = fund_me.withdraw(sender=account)
    print(f"Funded {value}")


def main():
    fund()
    withdraw()
