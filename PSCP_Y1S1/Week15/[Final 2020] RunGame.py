'''[Final 2020] RunGame'''
def cookie_run(run):
    '''[Final 2020] RunGame'''
    total = 0
    for i in range(1,len(run)):
        total += abs(int(run[i]) - int(run[i-1]))
    print(total)
cookie_run(("0 " + input()).split())
