'''Promotion_Milk'''
def milk(price, pro_pha, bottle, money):
    '''milk'''
    if not money:
        total_bottle = 0
    elif not pro_pha:
        total_bottle = money//price
    else:
        total_money = 0
        total_pha = 0
        total_bottle = 0
        while total_money + price <= money:
            total_money += price
            total_pha += 1
            total_bottle += 1
            if total_pha >= pro_pha:
                total_pha -= pro_pha
                total_bottle += bottle
                total_pha += bottle
    print(int(total_bottle))
milk(float(input()), int(input()), int(input()), float(input()))
