'''[Final 2019] Sxrt'''
def sxrt(num):
    '''sxrt'''
    temp_lst = []
    while num != "END":
        num = int(num)
        temp_lst.append(num)
        num = input()
    for _ in range(len(temp_lst)-1):
        print(temp_lst.pop(temp_lst.index(min((temp_lst)))))
    if temp_lst:
        print(max(temp_lst))
sxrt(input())
