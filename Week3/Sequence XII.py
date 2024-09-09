"""Sequence XII"""
def sequence(num):
    """Sequence XII"""
    for i in range(-num + 1, num, 1): # if num==3: i = -2 -1 0 1 2 (มี5ตัวก็เลยทำไป5รอบ)
        for j in range(-num + 1, num, 1): #if num==2: j = -2 -1 0 1 2
            print(f"{num - abs(abs(i)-abs(j)):>02}", end = " ") #r_1 = 3 | r_2 = 2 (iตัวแรกลบjจนครบทุกตัว)
        print()
sequence(int(input()))
