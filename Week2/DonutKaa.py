"""Donut"""
def main(price,buy,free,want):
    """Donut"""
    donut = 0 #start Donut
    pro = buy + free #Promotion e.g 5 + 4
    round_= want // pro #จำนวนโปรที่ซื้อ e,g 11 // 9
    if not want: #ไม่อยากด้ายย
        print("0 0")
    if want > 0: #ถ้าต้องการ e.g 1 > 0
        donut = pro * round_ #จำนวนโดนัทติดโปร e.g 9*1
        left = want - donut #ที่เหลือจากที่ต้องการ e.g 11-9
        if left > buy: #ถ้าที่เหลือมากกว่าจำนวนที่ต้องซื้อ
            left = buy 
        if left >= buy: #ถ้าที่เหลือ มากกว่า หรือ เท่ากับ จำนวนที่ต้องซื้อ
            donut += pro #จำนวนโดนัท เท่ากับ จำนวนโดนัท + โปร 
        else:
            donut += left #จำนวนโดนัท บวกกับ ที่เหลือ e,g 9 + 2
        print(f"{price * round_ * buy + ( left * price )} {donut}")
main(int(input()),int(input()),int(input()),int(input()))
