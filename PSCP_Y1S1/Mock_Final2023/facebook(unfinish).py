'''facebook'''
def facebook(ship):
    '''facebook'''
    list_friend = []
    while True:
        if "?" in ship:
            mul = ship.split(" ? ")
            break
        ship = ship.split(" <-> ")
        list_friend.append(ship)
        ship = input()
    for i in list_friend:
        if mul[0] in i:
            set_1 = set(i)
        if mul[1] in i:
            set_2 = set(i)
    print(list_friend)
facebook(input())
