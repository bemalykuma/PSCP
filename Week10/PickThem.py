'''PickThem'''
import json
def pick_pair(num):
    '''PickThem'''
    even = 0
    num_list = json.loads(num)
    for i in num_list:
        if not i % 2:
            print(i)
            even += 1
    if not even:
        print("Nope")
pick_pair(input())
