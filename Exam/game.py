"""Game"""
def game(score_a, score_b):
    """Game"""
    score_a_win = score_a // 3
    score_b_win = score_b // 3
    a_win_not_b = not score_b and not score_a % 3
    b_win_not_a = not score_a and not score_b % 3
    both_win = not score_b % 3 and not score_a % 3
    if score_a - (score_a_win * 3) == score_b - (score_b_win * 3):
        draw = score_a - (score_a_win * 3)
    elif both_win or a_win_not_b or b_win_not_a:
        draw = 0
    else:
        draw = "Error"
    print(draw)
game(int(input()), int(input()))
