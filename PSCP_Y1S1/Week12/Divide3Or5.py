'''Divide3Or5'''
def plus(num):
    '''Divide3Or5'''
    print(sum(list(i for i in range(3,num+1) if not i%3 or not i%5)))
plus(int(input()))
