pragma solidity ^0.4.24;

contract Organ {
    struct kidney {
        uint id;
        uint date;
        string ipfsAddress;
        bool active;
    }

    uint lastKidneyId;
    uint[] kidneyIds;
    mapping(uint => kidney) kidneys;

    event KidneyCreated(
        uint id,
        uint date,
        string ipfsAddress
        );

    constructor() public {
        lastKidneyId = 0;
    }

    function createKidney(string _ipfsAddress) public {
        kidneys[lastKidneyId] = kidney(lastKidneyId, now, _ipfsAddress,true);
        kidneyIds.push(lastKidneyId);
        lastKidneyId++;
        emit KidneyCreated(lastKidneyId, now, _ipfsAddress);
    }

    function getKidneyIds() public view returns (uint[]) {
        return kidneyIds;
    }

    function getKidney(uint id) public kidneyExists(id) view  
    returns (
        uint,
        uint,
        string,
        bool
    ) {
        return (id,
        kidneys[id].date,
        kidneys[id].ipfsAddress,
        kidneys[id].active
        );
    }
    
    function toggleActive(uint id) public kidneyExists(id)  {
        kidneys[id].active = false;
    }
     
    modifier kidneyExists(uint id) {
        if (kidneys[id].id == 0) {
            revert();
        }
        _;
    }
}
