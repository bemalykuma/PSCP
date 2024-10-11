'''3nPlus1'''
def plus(num):
    '''3nPlus1'''
    while num > 0:
        count = 1
        while num > 1:
            if not num%2:
                num = num/2
            else:
                num = num*3 +1
            count += 1
        print(count)
        num = int(input())
plus(int(input()))
