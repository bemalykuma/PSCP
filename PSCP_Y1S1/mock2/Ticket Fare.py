'''Ticket Fare'''
def train(station, pro_1, price_pro_1, pro_2, price_pro_2, price_pro_3):
    '''how much'''
    start = int(input())
    end = int(input())
    if end >= start: #หามากสุดน้อยสุดในกรณีที่ เลขสถานีที่ขึ้น มากกว่า เลขสถานีที่ลง
        mx,mn = end,start
    else:
        mx,mn = start,end
    if end > station or start > station:
        pay = "Error"
    else:
        amount = 0
        pay = 0
        amount = mx - pro_1 #สถานีที่เหลือหลังจากเข้าโปร1 ดักในกรณีไม่เข้าโปร1
        if 0 < mn <= pro_1+mn and pro_1:
            pay = price_pro_1
            amount = mx - (pro_1 + mn) #สถานีที่เหลือหลังจากเข้าโปร1 ของแท้
        if 0 < amount:
            pro_2_station = abs(amount - (abs(amount - pro_2))) #ในกรณีที่สถานีที่เหลือมากกว่าโปร2
            if not pro_1:
                pro_2_station -= 1 #ถ้าไม่เข้าโปรแรก ปล.จ่ายตอนลงเลยลบราคาตอนขึ้นออก
            elif amount <= pro_2: #ถ้าสถานีที่เหลือไม่เกินโปร2
                pro_2_station = amount
            pay_pro_2 = pro_2_station*price_pro_2
            pay += pay_pro_2
            if amount - pro_2 > 0: #pro_3
                pay += (amount - pro_2) * price_pro_3
    print(pay)
train(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))
