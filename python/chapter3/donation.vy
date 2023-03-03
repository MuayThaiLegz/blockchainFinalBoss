struct DonaturDetail:
    sum: uint256(wei)
    name: bytes2[100]
    time: timestamp

donatur_details: external(map(address, DonaturDetail))

donaturs: external(address[10])

donatee: external(address)

index: int128

@external
def __init__():
    self.donatee = msg.sender

@payable
@external
def donate(name: bytes[100]):
    assert msg.value >= as_wei_value(1, "ether")
    assert self.index < 10

    self.donatur_details[msg.sender] = DonaturDetail({
                                         sum: msg.value,
                                         name: name,
                                         time: block.timestamp
                                       })

    self.donaturs[self.index] = msg.sender
    self.index += 1

@external
def withdraw_donation():
    assert msg.sender == self.donatee

    send(self.donatee, self.balance)
