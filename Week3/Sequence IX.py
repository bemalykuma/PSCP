"""Sequence IX"""
def main(num):
    """Sequence IX"""
    for i in range(1 ,num+1):
        for j in range((num) - i):
            print("  ", end = " ")
        for j in range(1, i):
            print(f"{j:02}", end = " ")
        for i in range(i, 0, -1):
            print(f"{i:02}" , end = " ")
        print()
main(int(input()))
