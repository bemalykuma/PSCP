'''GCD_v1'''
def gcd(a, b):
    '''GCD_v1'''
    while b:
        a, b = b, a % b
    print(a)
gcd(int(input()), int(input()))
