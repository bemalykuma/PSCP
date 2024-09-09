"""RockPaperScissor"""
def main(paoyingshup):
    """RockPaperScissor"""
    result = ""
    score_a = 0
    score_b = 0
    for i in paoyingshup:
        result += i
        if result in ("RR", "SS", "PP"):
            result = ""
        elif result in ("PR", "SP", "RS"):
            score_a += 1
            result = ""
        elif result in ("RP", "SR", "PS"):
            score_b += 1
            result = ""
    if score_a > score_b:
        print(f"A win {score_a}-{score_b}")
    elif score_a < score_b:
        print(f"B win {score_b}-{score_a}")
    else:
        print(f"DRAW {score_a}")
main(input())
