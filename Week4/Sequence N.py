"""Sequence N"""
def main(num):
    """Sequence N"""
    for i in range(num):
        for j in range(num):
            if j in ( 0, num-1, i ):
                print( "*", end = "" )
            else:
                print( " ", end = "" )
        print()
main(int(input()))
