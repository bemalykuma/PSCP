'''Apartment'''
def apartment(room, price, rent, add, reduce_):
    '''Apartment'''
    income = 0
    normal = price*rent
    income_1 = (rent - 1) * (price+reduce_)
    if rent < room:
        income = (price - ((room-rent)*add)) * room
    if max([income, normal, income_1]) == income:
        print(income)
        print(room)
    elif max([income, normal, income_1]) == normal:
        print(normal)
        print(rent)
    else:
        print(income_1)
        print(rent-1)
apartment(int(input()), int(input()), int(input()), int(input()), int(input())) 
