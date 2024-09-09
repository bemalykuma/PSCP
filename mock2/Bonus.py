'''Bonus'''
def bonus(money, year, month):
    '''bonus'''
    if month >= 10:
        year += 1
    get = money * year
    if year > 20:
        get = money * 20
    if get > 1000000:
        get = 1000000
    elif get < 5000:
        get = 5000
    print(get)
bonus(int(input()), int(input()), int(input()))
