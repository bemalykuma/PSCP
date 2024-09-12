'''Sequence XXX'''
def sequence_xxx(size, num):
    '''Sequence XXX'''
    for i in range(size):
        if not i or i == size-1:
            for _ in range(num):
                print("*" * size, end = ' ')
            print()
        else:
            for _ in range(num):
                for j in range(size):
                    if i == j or not j or j == size - 1 or j == size - 1 - i:
                        print("*", end = '')
                    else:
                        print(" ",end = '')
                print(" ", end = '')
            print()
sequence_xxx(int(input()), int(input()))
