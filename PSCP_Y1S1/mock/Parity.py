"""Parity"""
def parity(bit, order):
    """Parity"""
    co_unt_one = 0
    for i in bit:
        if i == "1":
            co_unt_one += 1
    if order == "Even":
        if co_unt_one % 2:
            bit += "1"
        else:
            bit += "0"
    elif order == 'Odd':
        if not co_unt_one % 2:
            bit += "1"
        else:
            bit += "0"
    print(bit)
parity(input(), input())
