'''Area'''
def area(num):
    '''Area'''
    count = 0
    for _ in range(num):
        txt = input()
        for i in txt:
            if i != " ":
                count += 1
    print(count)
area(int(input()))
