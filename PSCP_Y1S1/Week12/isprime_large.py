'''isprime_large'''
def is_prime(n):
    '''is_prime'''
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True

def main(num):
    """main"""
    if is_prime(num) is True:
        print("YES")
    else:
        print("NO")
main(int(input()))
