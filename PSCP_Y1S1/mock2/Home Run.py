"""Home Run"""
def baseball(num, s_batter):
    """Home Run"""
    count = 0
    for _ in range(num):
        area = float(input())
        if s_batter > area:
            count += 1
    print(count)
baseball(int(input()), float(input()))
