"""Volleyball"""
def volley(win_team):
    """Volleyball"""
    score_a = 0
    score_b = 0
    for i in win_team:
        if i == "A":
            score_a += 1
        elif i == "B":
            score_b += 1
        if score_a == 25 and score_b == 25:
            if i == "A":
                score_a += 1
            elif i == "B":
                score_b += 1
            if abs(score_a - score_b) == 2:
                print(f"Set 1: A ({score_a}) | B ({score_b})")
                score_a = 0
                score_b = 0
        if score_b == 25 or score_a == 25:
            print(f"Set 1: A ({score_a}) | B ({score_b})")
            score_a = 0
            score_b = 0
volley(input())
