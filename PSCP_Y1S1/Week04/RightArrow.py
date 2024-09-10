"""Right Arrow"""
def main(width, height):
    """Right Arrow"""
    for i in range(height//2+1):
        for _ in range(2, i+2):
            print( " " , end = "" )
        for _ in range(width):
            print( "*" , end = "" )
        print()
    for i in range(height//2):
        for _ in range(height//2-1 , i ,-1):
            print( " " , end = "" )
        for _ in range(width):
            print( "*" , end = "" )
        print()
main(int(input()), int(input()))
