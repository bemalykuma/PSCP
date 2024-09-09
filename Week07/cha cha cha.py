"""Cha Cha Cha"""
import math
def cha(day):
    """Cha Cha Cha"""
    total = 0
    for _ in range(day):
        money_hour = math.ceil(float(input())) * 8720
        total += money_hour
    print(total)
cha(int(input()))
