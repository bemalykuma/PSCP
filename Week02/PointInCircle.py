"""PointInCircle"""
import math
def main(x,y,r,xn,yn):
    """PointInCircle"""
    d=math.sqrt((xn-x)**2+(yn-y)**2)
    if d<=r:
        print("True")
    else:
        print("False")
main(int(input()),int(input()),int(input()),int(input()),int(input()))
