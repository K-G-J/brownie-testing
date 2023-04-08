from brownie import SimpleStorage, accounts


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f'SimpleStorage Address: {simple_storage.address}')
    return simple_storage


def main():
    deploy_simple_storage()
