"""IT Bussiness"""
def bank(money_in_bank, current_money):
    """bank"""
    error = 0
    operation = input()
    while operation != "end":
        if operation[:2] == "D ":
            money = float(operation[2:])
            if current_money >= money:
                current_money -= money
                money_in_bank += money
                error = 0
            else:
                error += 1
        elif operation[:2] == "W ":
            money = float(operation[2:])
            if money_in_bank >= money:
                money_in_bank -= money
                current_money += money
                error = 0
            else:
                error += 1
        if error == 3:
            break
        operation = input()
    print(f"{money_in_bank:.02f}")
    print(f"{current_money:.02f}")
bank(float(input()), float(input()))
