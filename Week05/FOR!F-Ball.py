"""FOR!F-Ball"""
def main(position):
    """FOR!F-Ball"""
    ball = 1
    for i in position:
        if i == "A":
            if ball == 1:
                ball = 2
            elif ball == 2:
                ball = 1
        elif i == "B":
            if ball == 2:
                ball = 3
            elif ball == 3:
                ball = 2
        elif i == "C":
            if ball == 3:
                ball = 1
            elif ball == 1:
                ball = 3
    print(ball)
main(input())
