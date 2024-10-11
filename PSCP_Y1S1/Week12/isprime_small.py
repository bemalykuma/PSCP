'''isprime_small'''
def is_prime(n):
    '''is_prime'''
    count = 0
    for i in range(2, n+1):
        if not n % i:
            count += 1
    return count

def main(num):
    """main"""
    if is_prime(num) == 1:
        print("Yes")
    else:
        print("No")
main(int(input()))
