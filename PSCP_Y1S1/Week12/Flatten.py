'''Flatten'''
import json
def flatten(powder):
    '''Flatten'''
    n_powder = ""
    for i in powder:
        if not i in ("[]"):
            n_powder += i
    n_powder = "[" + n_powder + "]"
    list_powder = json.loads(n_powder)
    list_powder.sort()
    list_powder.reverse()
    print(list_powder)
flatten(input())
