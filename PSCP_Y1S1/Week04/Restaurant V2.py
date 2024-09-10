"""Restaurant"""
def main(price, pro, per, add):
    """Restaurant"""
    price_reduce = price * (1-(per/100))
    price_add_reduce = (price + add) * (1-(per/100))
    if price >= pro:
        if price_reduce < price_add_reduce:
            print(f"No {price_add_reduce-price_reduce:.03f}")
        else:
            print("Yes")
    elif price + add >= pro:
        pay = abs(price - price_add_reduce)
        if price_add_reduce < price:
            print(f"Yes {pay:.03f}")
        elif price_add_reduce > price:
            print(f"No {pay:.03f}")
        else:
            print("Yes")
    elif price + add < pro and add > 0:
        print(f"No {add:.03f}")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
