'''LineSorting'''
def sorting(num):
    '''LineSorting'''
    txt_len_ls = []
    num_list = []
    new_list = []
    for _ in range(num):
        text = input()
        length = len(text)
        txt_len_ls.append(text)
        txt_len_ls.append(length)
        num_list.append(txt_len_ls)
        new_list.append(text)
        new_list.append(length)
        txt_len_ls = []
    for i in num_list:
        txt_len_ls.append(i[1])
    txt_len_ls.sort()
    for i in txt_len_ls:
        print(new_list[new_list.index(i)-1])
sorting(int(input()))
