"""EuclideanDistance2D"""
import math
def main(q1,q2,p1,p2):
    """EuclideanDistance2D"""
    ans=math.sqrt((q1-p1)**2+(q2-p2)**2)
    print(ans)
main(float(input()),float(input()),float(input()),float(input()))
