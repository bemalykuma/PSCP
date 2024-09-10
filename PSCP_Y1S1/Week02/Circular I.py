"""Circular I"""
import math
def main(x,y,r,xn,yn):
    """Circular I"""
    d=math.sqrt((xn-x)**2+(yn-y)**2)
    if d<=r:
        print("Yes")
    else:
        print("No")
main(float(input()),float(input()),float(input()),float(input()),float(input()))
