# brownie-simple-message

This is a dApp built with brownie. The user can get a message from the blockchain and update it.

## Requirements:

- brownie: https://github.com/eth-brownie/brownie
- yarn: https://classic.yarnpkg.com/en/
- ganache-cli: https://www.npmjs.com/package/ganache-cli

## Setup

```
   # Install OpenZeppelin v4
   $ brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0

   # compile the app
   $ brownie compile

   #run the deploy.py script
   $ brownie run scripts/deploy.py
```

## Tests

### How to test locally

```
# run all tests:
$ brownie test

# run only one test, for example test_updating_message:
$ brownie test -k test_updating_message

# run post mortem tests to debug error:
$ brownie test -pdb

# run all tests and show more detailed info:
$ brownie test -s
```

### How to deploy to a testnet

#### Option 1: without verification

Documentation example of the first steps: https://chain.link/bootcamp/brownie-setup-instructions

1. Create an account, for example using MetaMask.
1. Switch into a testnet.
1. Fund your account, for example using a Faucet.
1. Signup in Infura (https://infura.io/) and create a project. Call it "brownie-simple-message".
1. Inside that project, select the testnet.
1. Save the `WEB3_INFURA_PROJECT_ID` value in the `.env` file
1. In **brownie**, you can select the network using the `--network` flag and the network name, for example `kovan`:

   `brownie run scripts/deploy.py --network kovan`

Then, you will see the transaction hash and the contract. You can also inspect in etherscan.

#### Option 2: with verification

In this option you can publish the source code in etherscan and a checkmark will appear in etherscan as a sign of verification.

1. Signup in Etherscan (https://etherscan.io/), login and go to API-KEYs section. Then create an API-KEY. You have to set a name, for example "verify_brownie".
1. Once you have the API-KEY, copy and paste it in the `.env` file as the `ETHERSCAN_TOKEN` value.
1. In `deploy.py` file, inside the `deploy` method, pass `publish_source=True` as the last parameter.
