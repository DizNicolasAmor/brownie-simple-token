from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
is_local_environments = network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if is_local_environments:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
