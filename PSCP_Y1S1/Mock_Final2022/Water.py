'''Water'''
def water(month, water_per_m3, over_m3, over_per_m3, less):
    '''WAter'''
    ans = 0
    for _ in range(month):
        water_per_month = float(input())
        if water_per_month > over_m3:
            pay = (water_per_m3*over_m3) + (water_per_month-over_m3)*over_per_m3
        else:
            pay = water_per_month * water_per_m3
        if pay <= less:
            pay = 0
        ans += pay
    print(f"{ans:.2f}")
water(int(input()), float(input()), float(input()), float(input()), float(input()))
