'''Tax'''
def tax(year, cc):
    '''Tax'''
    total = 0
    total = (total + 600*0.5 if cc - 600 > 0 else total + cc * 0.5)
    if cc - 1800 >= 0:
        total += (1800 - 600) * 1.50
        total += (cc - 1800) * 4
    elif 600 < cc < 1800:
        total += (cc - 600) * 1.50
    if year == 6:
        total -= total * (10/100)
    elif year == 7:
        total -= total * (20/100)
    elif year == 8:
        total -= total * (30/100)
    elif year == 9:
        total -= total * (40/100)
    elif year >= 10:
        total -= total * (50/100)
    print(f"{total:.2f}")
tax(int(input()), int(input()))
