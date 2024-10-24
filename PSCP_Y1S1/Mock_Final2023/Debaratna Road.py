'''Debaratna Road'''
def road(km):
    '''Debaratna Road'''
    if 0 <= km <= 5.032:
        print("Bangkok")
    elif 5.032 < km <= 35.477:
        print("Samut Prakarn")
    elif 35.477 < km <= 52.900:
        print("Chachoengsao")
    elif 52.900 < km <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
road(float(input()))
