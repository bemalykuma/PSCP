'''Factors'''
def factor(num):
    '''Factors'''
    for _ in range(num):
        n = int(input())
        prime = 2
        result = []
        while n > 1:
            count = 0
            while not n%prime:
                n = n//prime
                count += 1
            if count > 0:
                if count > 1:
                    result.append(f"{prime}**{count}")
                else:
                    result.append(str(prime))
            prime += 1
        print(" x ".join(result))
factor(int(input()))
