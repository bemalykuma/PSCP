'''Stamps'''
def stamps(num, eat, get_stamps, stamps_pro, reduce):
    '''collect stamps'''
    total_price = 0
    total_stamps = 0
    for _ in range(num):
        bill = int(input())
        while total_stamps >= stamps_pro and bill > 0:
            total_stamps -= stamps_pro
            bill -= reduce
        if bill < 0:
            bill = 0
        total_price += bill
        if bill >= eat:
            total_stamps += (bill // eat) * get_stamps
    print(total_price)
    print(total_stamps)
stamps(int(input()), int(input()), int(input()), int(input()), int(input()))
