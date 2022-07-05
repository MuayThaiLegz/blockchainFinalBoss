pragma solidity  0.5.5;

contract Onboarding {
  address private admin; // We are the owners
  
  mapping(string => address) private charitieTokens;

  constructor(address _admin) public {
        admin = _admin;
  }
  
  modifier isAdmin {  
    require(msg.sender == admin, 'Only admin can access this function');
    _;  
  }

  function addToken(address charityAdmin, string memory cryptoName) public isAdmin returns (address) {
    address charityAddress = charityAdmin;
    charitieTokens[cryptoName] = charityAddress;
    return charityAddress;
  }

  function getCharityTokenAddress(string memory cryptoName) public view returns (address) {
    return charitieTokens[cryptoName];
  }
}