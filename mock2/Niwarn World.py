"""Niwarn World"""
import math
def func_x(n):
    """Function X"""
    ans = 2 + ((math.log2(n**2)) / ((2 * n) * (math.log2(n))))
    return ans

def func_y(n, s):
    """Function Y"""
    ans = ((math.sin(math.radians(30)) + math.sqrt(2 * s)) / (func_x(n) + 3))
    return ans

def func_z(k):
    """Function Z"""
    ans = func_y(k,k)**2 + ((8456 * (func_x(k)**4)) / (24 * k))
    return ans

def position(n, s, k):
    """Position"""
    print(f"X: {func_x(n):.01f}, Y: {func_y(n, s):.01f}, Z: {func_z(k):.01f}")
position(float(input()), float(input()), float(input()))
