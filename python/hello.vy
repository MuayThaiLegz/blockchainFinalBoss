name: public(String[24])

@external

def __init__():
    self.name = "Javier Barrios"

@external
def change_name(new_name: String[24]):
    self.name = new_name

@external
def say_hello() -> String[32]:
    return concat("Hello, ", self.name)