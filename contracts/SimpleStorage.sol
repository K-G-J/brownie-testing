//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract SimpleStorage {
    uint256 public number;

    function setNumber(uint256 _newNumber) public {
        require(_newNumber > 0, "invalid number");
        number = _newNumber;
    }
}
