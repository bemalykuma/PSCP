'''Kabata'''
def kabata():
    '''Kabata'''
    for _ in range(int(input())):
        text = input()
        if not "baka" in text:
            text = text.replace("ta","").replace("bakka","").replace("ka","").replace("ba","")
        if not text:
            print("yes")
        else:
            print("no")
kabata()
