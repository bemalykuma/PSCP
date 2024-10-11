'''Difference'''
def difference(num_a, num_b):
    '''Find the difference of set'''
    set_a = set()
    set_b = set()
    for _ in range(num_a):
        set_a.add(int(input()))
    for _ in range(num_b):
        set_b.add(int(input()))
    print(*(sorted(set_a - set_b)))
difference(int(input()), int(input()))
