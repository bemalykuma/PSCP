"""Sequence IV"""
def main(num):
    """Sequence IV"""
    result = num-6
    for _ in range(1):
        for j in range(num,0,-1):
            print(j,end=" ")
            if j==result:
                print()
                result -= 7
main(int(input()))
