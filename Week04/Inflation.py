"""Inflation"""
def main(price, year):
    """Inflation"""
    if not year:
        ans = price * 1000//10
        print(f"{ans/100:.2f}")
    elif not price:
        print("0.00")
    else:
        price = int(price * 100)
        for _ in range(year):
            price += ( price * 381 )//10000
        print(f"{price//100}.{price%100:02}")
main(float(input()), int(input()))
