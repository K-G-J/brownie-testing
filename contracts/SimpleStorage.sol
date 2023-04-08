//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.19;

contract SimpleStorage {
    uint256 public number;

    event NumberChanged(uint256 oldNum, uint256 newNum);

    function setNumber(uint256 _newNumber) public {
        require(_newNumber > 0, "invalid number");
        uint256 oldNum = number;
        number = _newNumber;

        emit NumberChanged(oldNum, number);
    }
}
