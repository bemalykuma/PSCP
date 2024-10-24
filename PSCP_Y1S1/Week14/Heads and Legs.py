'''Heads and Legs'''
def cage(heads, leg):
    '''cage'''
    rabbit = leg//4
    bird = heads - rabbit
    if bird * 2 == leg - rabbit*4:
        print(rabbit,bird)
    else:
        print("Impossible")
cage(int(input()), int(input()))
