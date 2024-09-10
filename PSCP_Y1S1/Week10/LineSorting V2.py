'''LineSorting'''
def sorting(num):
    '''LineSorting'''
    num_list = []
    for _ in range(num):
        text = input()
        num_list.append(text)
    num_list.sort(key=len)
    for i in num_list:
        print(i)
sorting(int(input()))
