"""Sequence VI"""
def main(num):
    """Sequence VI"""
    for i in range(num):
        for j in range(num,i+1,-1):
            print("  ",end=" ")
        for j in range(1,i+2):
            print(f"{j:02}",end=" ")
        print()
main(int(input()))
