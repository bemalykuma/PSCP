'''BTU'''
def room_area_2(n):
    '''Recommended air Conditioner capacity 2'''
    ans = 0
    if 551 <= n <= 700:
        ans = 14000
    elif 701 <= n <= 1000:
        ans = 18000
    elif 1001 <= n <= 1200:
        ans = 21000
    elif 1201 <= n <= 1400:
        ans = 23000
    elif 1401 <= n <= 1500:
        ans = 24000
    elif 1501 <= n <= 2000:
        ans = 30000
    elif 2001 <= n <= 2500:
        ans = 34000
    return ans

def room_area(n):
    '''Recommended air Conditioner capacity'''
    ans = 0
    if 100 <= n <= 150:
        ans = 5000
    elif 151 <= n <= 250:
        ans = 6000
    elif 251 <= n <= 300:
        ans = 7000
    elif 301 <= n <= 350:
        ans = 8000
    elif 351 <= n <= 400:
        ans = 9000
    elif 401 <= n <= 450:
        ans = 10000
    elif 451 <= n <= 550:
        ans = 12000
    elif n > 550:
        ans = room_area_2(n)
    return ans

def btu(area, high, people, hot, bright):
    '''BTU'''
    btu_normal = room_area(area)
    add = 0
    if high > 8:
        add += (high - 8) * 1000
    if people > 2:
        add += (people - 2) * 600
    if hot == "kitchen":
        add += 4000
    pay = btu_normal + add
    if bright == "facing the sun":
        pay += pay*(10/100)
    elif bright == "shaded":
        pay -= pay*(10/100)
    print(int(pay))
btu(int(input()), int(input()), int(input()), input(), input())
