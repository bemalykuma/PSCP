'''Dart'''
def dart(n):
    '''dart'''
    result = 0
    for _ in range(n):
        position = input().split()
        x, y = int(position[0]), int(position[-1])
        distance = ((0-x)**2+(0-y)**2)**0.5
        if distance <= 2:
            result += 5
        elif 2 < distance <= 4:
            result += 4
        elif 4 < distance <= 6:
            result += 3
        elif 6 < distance <= 8:
            result += 2
        elif 8 < distance <= 10:
            result += 1
    print(result)
dart(int(input()))
