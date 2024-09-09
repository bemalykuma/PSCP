"""COFFEE SHOP"""
def promotion(price, per_1, per_2, pro, buy):
    """Coffee promotion"""
    pro_1 = price + (buy - 1) * (price - (price * (per_1 / 100)))
    pro_2 = (price * buy) - (((price * buy) * (per_2 / 100)))
    if price * buy >= pro and pro_2 <= pro_1:
        print(2)
        print(f"{pro_2:.2f}")
    else:
        print(1)
        print(f"{pro_1:.2f}")
promotion(float(input()), float(input()), float(input()), float(input()), int(input()))
