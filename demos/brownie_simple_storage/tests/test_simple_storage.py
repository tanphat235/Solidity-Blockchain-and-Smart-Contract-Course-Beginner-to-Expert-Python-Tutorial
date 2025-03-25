from ape import project, accounts, networks

with networks.ethereum.local.use_default_provider():
    faucet = accounts.test_accounts[0]
    my_account = accounts.load("test_account")
    faucet.transfer(my_account, "100 ether")

account = accounts.load("test_account")
account.set_autosign(True)


def test_deploy():
    # Arrange
    simple_storage = project.SimpleStorage.deploy(sender=account)
    # Act
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    simple_storage = project.SimpleStorage.deploy(sender=account)
    # Act
    expected = 15
    simple_storage.store(expected, sender=account)

    # Assert
    assert simple_storage.retrieve(sender=account) == 22
