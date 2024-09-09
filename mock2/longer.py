"""longer"""
import math
def line(rad, widgth, long_):
    """longer"""
    circle = 2 * math.pi * rad
    rectangle = (widgth * 2) + (long_ * 2)
    result = abs(circle - rectangle)
    if circle > rectangle:
        print("Circle is longer")
    elif rectangle > circle:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{result:.05f}")
line(float(input()), float(input()), float(input()))
