// JavaScript source code
var web3 = require('web3');

if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider);
} else {
    web3 = new Web3(new
        Web3.providers.HttpProvider("http://localhost:8545"));
}

web3.eth.defaultAccount = web3.eth.accounts[0];

var EscrowcontractFactory = web3.eth.contract([{ "inputs": [{ "internalType": "address", "name": "_buyer", "type": "address" }, { "internalType": "address payable", "name": "_seller", "type": "address" }, { "internalType": "uint256", "name": "_price", "type": "uint256" }], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "buyer", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "confirmDelivery", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "currState", "outputs": [{ "internalType": "enum Escrow.State", "name": "", "type": "uint8" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [], "name": "initContract", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "isBuyerIn", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "isSellerIn", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "price", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "seller", "outputs": [{ "internalType": "address payable", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "withdraw", "outputs": [], "stateMutability": "payable", "type": "function" }]);
var EscrowcontractInstace = EscrowcontractFactory.at('0x6628E0775cF09a5e33224718bf59B609087d423D');


console.log(`Contract Address ${EscrowcontractInstace}`)


function refreshAccountsTable() {
    var innerHTML = "<td><td>Account</td><td>Balance<td>";

    for (var i = 0; i < eth.accounts.length; i++) {
            var account = eth.accounts[i];
            var balance = EscrowcontractInstace.coinBalance(account);
            innerHTML = innerHTML + "<tr><td>" + account + "</td><td>" + balance +  "</td></tr>";
        }

        $("#accountBalanceTable").html(innerHTML);
    }

function transferCoins() {
    var sender = $("#from").val();
    var recipient = $("#to").val();
    var tokensToTransfer = $("#amount").val();
    EscrowcontractInstace.safeTransferFrom
}


function callBuyer()
    var txn = Escrowcontract.buyer.call();{
        console.log("return value: " + txn);
    }

function callSeller()
    var txn = Escrowcontract.call(seller);{
console.log("return value: " + txn);
}
function myFunction() {
    var x = document.getElementById("txtValue").value;
    var txn = Escrowcontract.Matcher.call(x); {
    };
    console.log("return value: " + txn);

    document.getElementById("decision").innerHTML = txn;