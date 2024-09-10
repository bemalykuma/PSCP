"""Heron of Alexandria"""
import math
def tri(a, b, c):
    """Heron of Alexandria"""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"{area:.03f}")
tri(float(input()), float(input()), float(input()))
