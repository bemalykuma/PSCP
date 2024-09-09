"""Sequence III"""
def main(num):
    """Sequence III"""
    for i in range(1,num+1):
        for j in range(i):
            print(j+1,end=" ")
        print()
main(int(input()))
