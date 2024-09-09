"""Sequence IV"""
def main(num):
    """Sequence IV"""
    for _ in range(1):
        for j in range(1,num**2+1):
            if j == num+1:
                print()
            print(j,end=" ")
            if not j%num and j != num:
                print()
main(int(input()))
