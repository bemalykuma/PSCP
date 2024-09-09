"""Stair"""
def stair(limit_walk, step):
    """Stair"""
    count = 0
    ans = 0
    for _ in range(step):
        length_stair = int(input())
        ans += length_stair
        if ans == limit_walk:
            count += 1
            ans = 0
            length_stair = 0
        elif length_stair <= limit_walk < ans:
            ans = length_stair
            count += 1
        elif length_stair > limit_walk:
            count = str(count)
            count = "NO"
            break
    if 0 < length_stair <= limit_walk:
        count += 1
    print(count)
stair(int(input()), int(input()))
