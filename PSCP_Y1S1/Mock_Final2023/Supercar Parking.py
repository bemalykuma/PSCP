'''Supercar Parking'''
def super_car(park):
    '''Supercar Parking'''
    car = 0
    i = 1
    while i < len(park)-1:
        if (park[i-1] == "0" or park[i-1] == " ") and (park[i+1] == "0" or park[i+1] == " ") \
            and park[i] != "1":
            car += 1
            i += 2
        else:
            i += 1
    print(car)
super_car(" "+input()+" ")
