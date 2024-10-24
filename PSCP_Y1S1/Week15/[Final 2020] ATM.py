'''[Final 2020] ATM'''
def atm(money):
    '''[Final 2020] ATM'''
    order = input()
    while order != "END":
        money = (money + int(order[1:]) if order[0] == "D" else money - int(order[1:]))
        money = (0 if money < 0 else money)
        order = input()
    print(money)
atm(int(input()))
