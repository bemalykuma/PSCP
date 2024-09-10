"""Lotto"""
def lotto(congrat,num_two,front_three_1,front_three_2):
    """how much you get"""
    back_three_1 = input()
    back_three_2 = input()
    your_lotto = input()
    nearby_add = f"{(int(congrat) + 1):>06}"
    nearby_low = f"{(int(congrat) - 1):>06}"
    money = 0
    if nearby_add == "1000000":
        nearby_add = "000000"
    if nearby_low == "0000-1":
        nearby_low = 999999
    if your_lotto == congrat:
        money += 6000000
    if your_lotto in (str(nearby_add) , str(nearby_low)):
        money += 100000
    if your_lotto[-2:] == num_two:
        money += 2000
    if your_lotto[:3] == front_three_1:
        money += 4000
    if your_lotto[:3] == front_three_2:
        money += 4000
    if  your_lotto[3:] == back_three_1:
        money += 4000
    if  your_lotto[3:] == back_three_2:
        money += 4000
    print(money)
lotto(input(),input(),input(),input())
