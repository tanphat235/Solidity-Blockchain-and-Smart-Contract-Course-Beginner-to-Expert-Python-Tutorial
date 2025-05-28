from ape import project, accounts, networks, config
from scripts.helpful_scripts import get_account, deploy_mocks
from dotenv import load_dotenv

load_dotenv()

with networks.ethereum.local.use_default_provider():
    faucet = accounts.test_accounts[0]
    my_account = accounts.load("test_account")
    faucet.transfer(my_account, "100 ether")

    print(f"Active Network: {networks.active_provider.network.name}")


def deploy_fund_me():
    account = get_account()
    print(account)

    # if we are on persistent network like Sepolia, us the associated address
    # ortherwise, deploy mocks
    chain_id = networks.active_provider.network.chain_id
    active_network = networks.active_provider.network.name
    if chain_id == 11155111:  # Sepolia
        price_feed_address = config["networks"]["ethereum"][active_network][
            "eth_usd_price_feed"
        ]
    else:
        aggregator = deploy_mocks(account)
        price_feed_address = aggregator.address

    print(price_feed_address)
    fund_me = project.FundMe.deploy(
        price_feed_address,
        sender=account,
        publish=config["networks"]["ethereum"][active_network].get("verify"),
    )
    print(f"Contract deploy to {fund_me.address}")

    return fund_me


def main():
    print("Script is running...")
    deploy_fund_me()
    print("contractttttttttt", project.FundMe.deployments)
