'''GCD_v2'''
def gcd(a, b):
    '''GCD_v2'''
    while b:
        a, b = b, a % b
    print(a)
gcd(int(input()), int(input()))
