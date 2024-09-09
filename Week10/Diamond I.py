'''Diamond I'''
def diamond(down, width):
    '''Diamond I'''
    down_list = []
    width_list = []
    down_lst_tmp = []
    for _ in range(down):
        num_width = input().split()
        width_list.append(num_width)
    for i in range(width):
        for j in range(down):
            down_lst_tmp.append(int(width_list[j][i]))
        down_list.append(down_lst_tmp)
        down_lst_tmp = []
    for i in down_list:
        down_lst_tmp.append(sum(i))
    print(max(down_lst_tmp))
diamond(int(input()), int(input()))
