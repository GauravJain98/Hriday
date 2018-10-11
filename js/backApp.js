const Web3 = require('web3');
const contract = require('truffle-contract');
const fs = require('fs');

const organArtifacts = require('../build/contracts/Organ.json');

const Organ = contract(organArtifacts);

var app;
var accounts;
var account;

const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:8545'));
Organ.setProvider(web3.currentProvider);

if (typeof Organ.currentProvider.sendAsync !== 'function') {
    Organ.currentProvider.sendAsync = async () =>
        await Organ.currentProvider.send.apply(
            Organ.currentProvider,
            arguments
        );
}

web3.eth.getAccounts((err, accs) => {
    if (err != null) {
        console.error('There was an error fetching your accounts.');
        return;
    }
    if (accs.length == 0) {
        console.error(
            "Couldn't get any accounts! Make sure your Ethereum client is configured correctly."
        );
        return;
    }
    accounts = accs;
    console.log(accounts);
    Organ.deployed()
        .then(instance => console.log(instance))
        .catch(err => console.log(err));
});
