'''Duplicate I'''
def intersec(num_1, num_2):
    '''Duplicate I'''
    g_1 = set()
    g_2 = set()
    for _ in range(num_1):
        g_1.add(input())
    for _ in range(num_2):
        g_2.add(input())
    for i in sorted(g_1.intersection(g_2), reverse=True):
        print(i)
    if not g_1.intersection(g_2):
        print("Nope")
intersec(int(input()), int(input()))
