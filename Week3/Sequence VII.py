"""Sequence VII"""
def main(num):
    """Sequence VII"""
    for i in range(num):
        for j in range(1,i+2):
            print(j,end=" ")
        print()
    for i in range(num-1):
        for j in range(1,num-i):
            print(j,end=" ")
        print()
main(int(input()))
