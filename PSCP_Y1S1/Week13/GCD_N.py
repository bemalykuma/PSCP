'''GCD_N'''
import math
import functools
def gcd_n(num):
    '''find_GCD'''
    list_num = [int(input()) for _ in range(num)]
    print(functools.reduce(math.gcd, list_num))
gcd_n(int(input()))
