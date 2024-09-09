"""ChristmasTree"""
def main(leaves, tree):
    """ChristmasTree"""
    for i in range(1,leaves+1):
        for _ in range(leaves-i):
            print(" " , end = "" )
        for _ in range(1, i):
            print("*" , end = "" )
        for _ in range(i, 0 , -1):
            print("*" , end = "" )
        print()
    for _ in range(tree):
        print(" " * (leaves-2), end = "---")
        print()
main(int(input()), int(input()))
