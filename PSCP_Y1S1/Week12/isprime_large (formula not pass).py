'''isprime_large'''
def is_prime(num):
    '''is_prime'''
    check_num = round(num/6)
    formula_1 = (6 * check_num) + 1
    formula_2 = (6 * check_num) - 1
    if not num%5 and num!=5 or not num%37 and num != 37:
        print("NO")
    elif (num == formula_1 or num == formula_2 or num in (2,3,5)) and num != 1:
        print("YES")
    else:
        print("NO")
is_prime(int(input()))
