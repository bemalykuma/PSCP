"""Quadrant"""
def main(x,y):
    """Quadrant"""
    if x>0 and y>0:
        print("Q1")
    elif x<0<y:
        print("Q2")
    elif x<0 and y<0:
        print("Q3")
    elif y<0<x:
        print("Q4")
    elif not x and not y:
        print("O")
    elif not x and y>0 or y<0:
        print("Y")
    elif not y and x<0 or x>0:
        print("X")
main(int(input()),int(input()))
