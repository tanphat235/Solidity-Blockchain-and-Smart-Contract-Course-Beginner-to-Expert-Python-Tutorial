from ape import project


def read_contract():

    # Get the last deployment in SimpleStorage contract
    simple_storage = project.SimpleStorage.deployments[-1]

    print("simple_storageeeeeeeeeeeeeeeee", simple_storage)

    # Get the value of the last deployment
    print(simple_storage.retrieve())


def main():
    read_contract()
