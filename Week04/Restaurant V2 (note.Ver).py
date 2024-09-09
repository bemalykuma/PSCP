"""Restaurant"""
def main(price, pro, per, add):
    """Restaurant"""
    price_reduce = price * (1-(per/100))
    price_add_reduce = (price + add) * (1-(per/100))
    if price >= pro: #ราคามากกว่าโปร
        if price_reduce < price_add_reduce:
            print(f"No {price_add_reduce-price_reduce:.03f}") #ราคาที่บวกเพิ่มและคำนวณแล้ว ลบกับ ราคาเดิม(ก่อนเราซื้อเพิ่ม)ที่เราต้องจ่ายอยู่แล้ว
        else:
            print("Yes") #ราคาที่เราต้องจ่าย >= ราคาที่บวกเพิ่มก็คือคุ้มเพราะถึงจะบวกเพิ่มแต่ราคาที่เราต้องจ่ายก็เป็นราคาก่อนบวกเพิ่มอยู่แล้ว
    elif price + add >= pro: #price < pro
        pay = abs(price - price_add_reduce)
        if price_add_reduce < price:
            print(f"Yes {pay:.03f}")
        elif price_add_reduce == price:
            print("Yes")
        else:
            print(f"No {pay:.03f}")
    elif price + add < pro and add > 0:
        print(f"No {add:.03f}")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
