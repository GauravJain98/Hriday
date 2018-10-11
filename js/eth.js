// A $( document ).ready() block.
$(document).ready(function() {
    console.log('ready!');
});
// Initialize Web3
if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider);
} else {
    // Set the provider you want from Web3.providers
    web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
}
// Set Account
web3.eth.defaultAccount = web3.eth.accounts[0];

web3.eth.getAccounts().then(console.log);

// Set Contract Abi
var contractAbi = [
    {
        constant: false,
        inputs: [
            {
                name: 'id',
                type: 'uint256'
            }
        ],
        name: 'toggleActive',
        outputs: [],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'function'
    },
    {
        constant: false,
        inputs: [
            {
                name: '_ipfsAddress',
                type: 'string'
            },
            {
                name: '_author',
                type: 'string'
            }
        ],
        name: 'createKidney',
        outputs: [],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'function'
    },
    {
        constant: true,
        inputs: [
            {
                name: 'id',
                type: 'uint256'
            }
        ],
        name: 'getKidney',
        outputs: [
            {
                name: '',
                type: 'uint256'
            },
            {
                name: '',
                type: 'uint256'
            },
            {
                name: '',
                type: 'string'
            },
            {
                name: '',
                type: 'string'
            },
            {
                name: '',
                type: 'bool'
            }
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function'
    },
    {
        constant: true,
        inputs: [],
        name: 'getKidneyIds',
        outputs: [
            {
                name: '',
                type: 'uint256[]'
            }
        ],
        payable: false,
        stateMutability: 'view',
        type: 'function'
    },
    {
        inputs: [],
        payable: false,
        stateMutability: 'nonpayable',
        type: 'constructor'
    },
    {
        anonymous: false,
        inputs: [
            {
                indexed: false,
                name: 'id',
                type: 'uint256'
            },
            {
                indexed: false,
                name: 'date',
                type: 'uint256'
            },
            {
                indexed: false,
                name: 'ipfsAddress',
                type: 'string'
            },
            {
                indexed: false,
                name: 'author',
                type: 'string'
            }
        ],
        name: 'KidneyCreated',
        type: 'event'
    }
];
// Set Contract Address
var contractAddress = '0x68d05db05445cdaad713955adc0734570ebd5337'; // Add Your Contract address here!!!

var contract = new web3.eth.Contract(contractAbi, contractAddress);

contract.methods
    .createKidney(organ, author)
    .send(
        { from: '0xB8441d33e223D88D9A37d83d4921A12462F23848' },
        (error, result) => {
            console.log(error, result);
        }
    )
    .then(console.log);
