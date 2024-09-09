"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main(word,num1,num2,num3):
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    mx=0
    mid=0
    mn=0
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
    if word == "Ascend":
        print(f"{mn:.2f}, {mid:.2f}, {mx:.2f}")
    elif word == "Descend":
        print(f"{mx:.2f}, {mid:.2f}, {mn:.2f}")
main(str(input()),float(input()),float(input()),float(input()))
