from brownie import config, network, SimpleToken
from web3 import Web3
from scripts.helpers import get_account


def deploy_token(initial_supply=Web3.toWei(1, 'ether')):
    account = get_account()
    must_publish = config["networks"][network.show_active()].get("verify")
    print('Deploying Token...\n')

    simple_token = SimpleToken.deploy(
        initial_supply,
        { "from": account },
        publish_source=must_publish
    )

    print('Deployed!\n')
    print('Token name: "%s"'  % simple_token.name())
    print('Token symbol: "%s"'  % simple_token.symbol())
    print('Total supply: "%s"\n'  % simple_token.totalSupply())

    return simple_token

def main():
    deploy_token()
