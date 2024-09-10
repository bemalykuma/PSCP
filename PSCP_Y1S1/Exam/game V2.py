"""Game"""
def game(score_a, score_b):
    """Game"""
    if score_a % 3 == score_b % 3:
        print(score_a % 3)
    else:
        print("Error")
game(int(input()), int(input()))
