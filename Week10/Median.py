'''Median'''
import math
def median(num):
    '''Median'''
    my_list = []
    for _ in range(num):
        number = float(input())
        my_list.append(number)
    my_list.sort()
    if num%2:
        position = math.ceil(num/2)
        print(f"{my_list[position-1]:.3f}")
    else:
        position_1 = int(num/2)
        position_2 = int((num/2)+1)
        find_med = (my_list[position_1-1] + my_list[position_2-1])/2
        print(f"{find_med:.3f}")
median(int(input()))
