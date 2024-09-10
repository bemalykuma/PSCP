"""COFFEE SHOP"""
def promotion(price, per_next, per_reduce, pro, buy):
    """Coffee promotion"""
    pro_1 = price - (price * (per_next / 100))
    pro_1_pay = price + (pro_1 * (buy-1))
    pro_2 = (price * buy) - (((price * buy) * (per_reduce / 100)))
    if price * buy >= pro:
        if pro_1_pay < pro_2:
            ans = 1
        else:
            ans = 2
            pro_1_pay = pro_2
    else:
        ans = 1
    print(ans)
    print(f"{pro_1_pay:.2f}")
promotion(float(input()), float(input()), float(input()), float(input()), int(input()))
