from brownie import SimpleToken, accounts, network, config, exceptions
from scripts.deploy import deploy_token
from scripts.helpers import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from web3 import Web3
import pytest


def start_test():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    token = deploy_token()
    account1 = get_account()
    account2 = get_account(index=1)
    return token, account1, account2

def test_total_supply():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    initial_supply = Web3.toWei(1, 'ether')
    different_supply = Web3.toWei(2, 'ether')
    token = deploy_token(initial_supply)
    total_supply = token.totalSupply()
    assert total_supply == initial_supply
    assert total_supply != different_supply


def test_balance_of():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    token, account1, _ = start_test()
    balance = token.balanceOf(account1)
    assert balance > 0

def test_transfer():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    token, account1, account2 = start_test()
    start_balance_account1 = token.balanceOf(account1)
    start_balance_account2 = token.balanceOf(account2)
    transfer = token.transfer(account2, start_balance_account1, {'from': account1})
    end_balance_account1 = token.balanceOf(account1)
    end_balance_account2 = token.balanceOf(account2)
    assert (end_balance_account2 == start_balance_account1 + start_balance_account2) and (end_balance_account1 == 0)

def test_allowance():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    token, account1, account2 = start_test()
    start_balance_account1 = token.balanceOf(account1)
    allowance_start = token.allowance(account1, account2)
    approve = token.approve(account2, start_balance_account1, {'from': account1})
    allowance_end = token.allowance(account1, account2)
    assert allowance_end > allowance_start

def test_transfer_from():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    token, account1, account2 = start_test()
    start_balance_account1 = token.balanceOf(account1)
    start_balance_account2 = token.balanceOf(account2)
    approve = token.approve(account2, start_balance_account1, {'from': account1})
    token.transferFrom(account1, account2, start_balance_account1, {'from': account2})
    assert token.balanceOf(account1) == 0
    assert token.balanceOf(account2) == start_balance_account1 + start_balance_account2
