"""Circular II"""
import math
def main(x1,y1,r1,x2,y2):
    """Circular I"""
    r2=float(input())
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d<r1+r2:
        print("Yes")
    else:
        print("No")
main(float(input()),float(input()),float(input()),float(input()),float(input()))
