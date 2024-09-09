'''PickThem'''
def pick_pair(num_list):
    '''PickThem'''
    num = ''
    i = 0
    even = 0
    while i < (len(num_list)):
        if num_list[i].isnumeric():
            num += num_list[i]
            while num_list[i+1].isnumeric():
                num += num_list[i+1]
                i += 1
        if num.isnumeric():
            if not int(num) % 2:
                print(num)
                num = ''
                even += 1
            num = ''
        i += 1
    if not even:
        print("Nope")
pick_pair(input())
