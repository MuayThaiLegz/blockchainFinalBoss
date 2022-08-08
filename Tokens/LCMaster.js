export default {
    address: "0x5F314B872B103BC1C51b7c8588c9c9D4127452C0",
        "abi":  [
          {
            "inputs": [],
            "payable": true,
            "stateMutability": "payable",
            "type": "constructor"
          },
          {
            "anonymous": false,
            "inputs": [
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "LCNum",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "address",
                "name": "SAcc",
                "type": "address"
              },
              {
                "indexed": false,
                "internalType": "address",
                "name": "BAcc",
                "type": "address"
              },
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "Amt",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "bytes2",
                "name": "Stat",
                "type": "bytes2"
              },
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "DOI",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "DOE",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "address",
                "name": "LCAdd",
                "type": "address"
              }
            ],
            "name": "CreateLCSuccessful",
            "type": "event"
          },
          {
            "anonymous": false,
            "inputs": [
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "LCNum",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "address",
                "name": "SAcc",
                "type": "address"
              },
              {
                "indexed": false,
                "internalType": "address",
                "name": "BAcc",
                "type": "address"
              },
              {
                "indexed": false,
                "internalType": "uint256",
                "name": "Amt",
                "type": "uint256"
              },
              {
                "indexed": false,
                "internalType": "bytes2",
                "name": "Stat",
                "type": "bytes2"
              }
            ],
            "name": "ModifyLCSuccessful",
            "type": "event"
          },
          {
            "constant": true,
            "inputs": [],
            "name": "ERC20Interface",
            "outputs": [
              {
                "internalType": "contract ERC20",
                "name": "",
                "type": "address"
              }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
          },
          {
            "constant": false,
            "inputs": [
              {
                "internalType": "address",
                "name": "BAcc",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "SAcc",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "Amt",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "DOE",
                "type": "uint256"
              }
            ],
            "name": "createLC",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
          },
          {
            "constant": true,
            "inputs": [],
            "name": "lengthLC",
            "outputs": [
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
          },
          {
            "constant": true,
            "inputs": [
              {
                "internalType": "uint256",
                "name": "viewLCNo",
                "type": "uint256"
              }
            ],
            "name": "viewLC",
            "outputs": [
              {
                "internalType": "address",
                "name": "",
                "type": "address"
              },
              {
                "internalType": "address",
                "name": "",
                "type": "address"
              },
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              },
              {
                "internalType": "bytes2",
                "name": "",
                "type": "bytes2"
              },
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
              },
              {
                "internalType": "address",
                "name": "",
                "type": "address"
              }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
          },
          {
            "constant": false,
            "inputs": [
              {
                "internalType": "uint256",
                "name": "LCNum",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "SettleAmt",
                "type": "uint256"
              },
              {
                "internalType": "bytes2",
                "name": "Stat",
                "type": "bytes2"
              }
            ],
            "name": "modifyLC",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
          }
        ]
}