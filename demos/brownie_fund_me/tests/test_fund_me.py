from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIROMENT
from scripts.deploy import deploy_fund_me
from web3 import Web3
from ape import networks, accounts, exceptions
import pytest

account = get_account()


def test_can_fund_and_withdraw():
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee(sender=account)
    buffer = Web3.to_wei(0.0001, "ether")
    tx = fund_me.fund(value=entrance_fee + buffer, sender=account)
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee + buffer

    tx2 = fund_me.withdraw(sender=account)
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if networks.active_provider.network.name not in LOCAL_BLOCKCHAIN_ENVIROMENT:
        pytest.skip(
            "only for local testing"
        )  # for skip testing the local network like development or local

    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw(sender=bad_actor)
