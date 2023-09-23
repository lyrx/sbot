// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ZeroToOne {
    uint256 public storageVar;  // Storage variable declaration without initialization

    constructor() {
        // Initializing the storage variable in the constructor to a non-zero value
        storageVar = 5;
    }

    // Temporary variable inside a function (won't trigger the finding)
    function someFunction() public returns (uint256) {
        storageVar = 7;
        uint256 tempVar = 10;
        return tempVar;
    }
}
