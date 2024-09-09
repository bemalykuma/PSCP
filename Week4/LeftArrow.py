"""Left Arrow"""
def main(width, height):
    """Left Arrow"""
    for i in range(height//2+1):
        for _ in range(height//2 , i ,-1):
            print( " " , end = "" )
        for _ in range(width):
            print( "*" , end = "" )
        print()
    for i in range(height//2):
        for _ in range(1, i+2):
            print( " " , end = "" )
        for _ in range(width):
            print( "*" , end = "" )
        print()
main(int(input()), int(input()))
