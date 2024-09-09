"""Bill"""
def main(price):
    """bill"""
    service = price * 0.1
    if service < 50:
        price += 50
    elif service > 1000:
        price += 1000
    else:
        price += service
    print(f"{price*1.07:.2f}")
main(float(input()))
