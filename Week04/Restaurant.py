"""Restaurant"""
def main(price, pro, per, add):
    """Restaurant"""
    if price >= pro:
        if (price * ( 1 - (per/100))) < (( price + add ) * ( 1 - (per/100))):
            pay = ((price * ( 1 - (per/100)) - price) - ((( price + add ) *\
                ( 1 - (per/100))) - price))
            print(f"No {abs(pay):.3f}")
        else:
            print("Yes")
    elif price + add >= pro:
        pay = (( price + add ) * ( 1 - (per/100))) - price
        if not (( price + add ) * ( 1 - (per/100))) - price:
            print("Yes")
        elif ((price + add) * (1 - (per/100))) > price:
            print(f"No {pay:.3f}")
        else:
            print(f"Yes {abs(pay):.3f}")
    elif price < pro and not add:
        print("Yes")
    elif price + add < pro:
        pay = (price + add) - price
        print(f"No {pay:.3f}")
main(float(input()), float(input()), float(input()), float(input()))
