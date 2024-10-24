'''Promotion'''
def pro(pro_come, pro_pay, price_per_head, come):
    '''pro'''
    pay = 0
    promotion = come//pro_come
    payself = come - promotion*pro_come
    if promotion:
        pay += pro_pay * price_per_head * promotion
    if payself:
        pay += price_per_head * payself
    print(pay)
pro(int(input()), int(input()), int(input()), int(input()))
