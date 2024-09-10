"""LastStand"""
def last_digit(num_list):
    """LastStand"""
    length = len(num_list)
    for i in range(length):
        if num_list[i] in (',', ']'):
            print(num_list[i-1])
last_digit(input())
