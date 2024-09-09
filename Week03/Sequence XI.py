"""Sequence XI"""
def sequence(num):
    """Sequence XI"""
    for i in range(-num + 1, num, 1): # if num==2: i = -1 0 1 (มี3ตัวก็เลยทำไป3รอบ)
        for j in range(-num + 1, num, 1): #if num==2: j = -1 0 1
            if abs(i) > abs(j) - 1: #ex.round_1 if 1 > (1-1) | round_2 0 > abs(0-1) is False | round_3 เหมือน round_1
                print(f"{num - abs(i):>02}", end = " ") # R_1 and R_3 print 2-1 = 1
            else:
                print(f"{num - abs(j):>02}", end = " ") # R_2 print 2-0 = 2
        print()
sequence(int(input()))
