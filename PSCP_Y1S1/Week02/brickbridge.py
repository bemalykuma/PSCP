"""BrickBridge"""
def main(small,big,goal):
    """BrickBridge"""
    re=goal-big*5
    if big*5 > goal:
        use_b = goal//5
        re=goal-use_b*5
    if small>=re:
        print(re)
    else:
        print(-1)
main(int(input()),int(input()),int(input()))
