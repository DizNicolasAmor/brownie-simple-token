// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SimpleToken is ERC20 {
    string _tokenName = "Simple Token";
    string _tokenSymbol = "SIMPLE_TKN";

    constructor(uint256 initialSupply) ERC20(_tokenName, _tokenSymbol) {
        _mint(msg.sender, initialSupply);
    }
}
