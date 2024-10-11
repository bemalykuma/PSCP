'''CoPrimeV1'''
def co_prime(a, b):
    '''CoPrimeV1'''
    while b:
        a, b = b, a % b
    if a == 1:
        print("YES")
    else:
        print("NO")
    print(a)
co_prime(int(input()), int(input()))
