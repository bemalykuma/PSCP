'''PickThemAgain'''
def pick_mod(num):
    '''PickThemAgain'''
    num_list = num.split(" ")
    num_list.reverse()
    correct = 0
    for i in num_list:
        i = int(i)
        if not i % 3 or not i % 5:
            print(i)
            correct += 1
    if not correct:
        print("Nope")
pick_mod(input())
