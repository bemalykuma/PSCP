'''Promotion_Coke'''
def coke(price, pro_pha, new_price, want):
    '''coke'''
    if not want:
        total_price = 0
    elif not pro_pha:
        total_price = want * price
    else:
        total_price = 0
        total_pha = 0
        total_bottle = 0
        while total_bottle < want:
            if total_pha >= pro_pha:
                total_pha -= pro_pha
                total_price += new_price
                total_bottle += 1
                total_pha += 1
            else:
                total_price += price
                total_bottle += 1
                total_pha += 1
    print(total_price)
coke(int(input()), int(input()), int(input()), int(input()))
