'''All_Primes'''
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
    count = 0
    for i in range(2, num+1):
        if is_prime(i) is True:
            count += 1
    print(count)
main(int(input()))
