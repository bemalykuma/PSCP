"""Largest Number"""
def main(num1,num2,num3):
    """Largest Number"""
    mx=0
    mid=0
    mn=0
    num1=abs(num1)
    num2=abs(num2)
    num3=abs(num3)
    if num1 > num2 and num1 > num3:
        mx = num1
        if num2 > num3:
            mid= num2
            mn =num3
        else:
            mid=num3
            mn=num2
    elif num2 > num1 and num2 > num3:
        mx = num2
        if num1 > num3:
            mid= num1
            mn =num3
        else:
            mid=num3
            mn=num1
    else:
        mx = num3
        if num2 > num1:
            mid= num2
            mn =num1
        else:
            mid=num1
            mn=num2
    if mn%10 > mid%10 and mn%10 > mx%10:
        print(str(mn)+str(mx)+str(mid))
    else:
        print(str(mx)+str(mid)+str(mn))
main(int(input()),int(input()),int(input()))
