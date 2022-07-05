pragma solidity 0.5.5;


contract CharityChain {
    address admin;  // Charity's admin
  //  string public charityID; // Charity's charityID
    bytes32[] donors; //Charity donors;
    // uint constant MAX_LENGTH = 50; // max number of transactions returned for a search by donor

    struct Donation {
      uint amount; // Amount in specified crypto [Algo, Cosmos, Tezos, Polkadot]
      uint dateofRet; // DDMMYYYY format
      string message; // Any message
    }

    // Table of all owners
    mapping(address => bool) owners;

    // Maps each donor's nricHashes with the total donation counts 
    mapping(bytes32 => uint256) donationCounts;

    // Maps each donor's nricHashes with the table of donations
    mapping(bytes32 => mapping(uint256 => Donation)) donations;
    

    constructor(address _admin) public { //string memory charityID
        admin = _admin;
        owners[_admin] = true;
    

    }

    modifier isAdmin {
      require(msg.sender == admin, 'Only admin can access this function');
      _;
    }
    
    modifier isOwners {
    require(owners[msg.sender], 'Only owners can access this function');
      _;
    }

    function addOwner(address owner) public isAdmin {
      owners[owner] = true;
    }

    function checkOwner(address owner) public view returns (bool) {
      return owners[owner];
    } 

    function removeOwner(address owner) public isAdmin {
      owners[owner] = false;
    }

    function addDonation(bytes32 donorsdigitalSig, uint amount, uint date, string memory message) public isOwners {
      Donation memory newDonation = Donation(amount, date, message);
      uint size = donationCounts[donorsdigitalSig];
      donations[donorsdigitalSig][size] = newDonation;
      if (donationCounts[donorsdigitalSig] == 0) {
        donors.push(donorsdigitalSig);
      }
      donationCounts[donorsdigitalSig] = size + 1;
    }

    function getDonationCount(bytes32 donorsdigitalSig) public view returns (uint) {
      return donationCounts[donorsdigitalSig];
    }

    function getDonation(bytes32 donorsdigitalSig, uint index) public view returns (uint, uint, string memory) {
      Donation memory donation = donations[donorsdigitalSig][index];
      return (donation.amount, donation.dateofRet, donation.message);
    }

    function getDonors() public view returns (bytes32[] memory) {
      return donors;
    }
}


