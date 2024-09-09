"""Triangle I"""
def main(n1,n2,n3):
    """Triangle I"""
    mx=0
    mid=0
    mn=0
    if n1 > n2 and n1 > n3:
        mx = n1
        if n2 > n3:
            mid= n2
            mn =n3
        else:
            mid=n3
            mn=n2
    elif n2 > n1 and n2 > n3:
        mx = n2
        if n1 > n3:
            mid= n1
            mn =n3
        else:
            mid=n3
            mn=n1
    else:
        mx = n3
        if n2 > n1:
            mid= n2
            mn =n1
        else:
            mid=n1
            mn=n2
    ab=mid**2+mn**2
    def tri():
        if ab==mx**2:
            print("Yes")
        elif (mx-0.01)**2<=ab<=(mx+0.01)**2:
            print("Yes")
        else:
            print("No")
    tri()
main(float(input()),float(input()),float(input()))
