"""diamond"""
def diamond(num):
    """diamond"""
    for i in range(num):
        for j in range(num):
            if i == num//2:
                print("*" , end = "")
            elif j - i == num//2 or i + j == num//2:
                print("*" , end = "")
            elif i - j == num//2 or i + j == num+(num//2)-1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()
diamond(int(input()))
