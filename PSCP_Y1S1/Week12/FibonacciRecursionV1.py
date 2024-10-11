'''FibonacciRecursionV1'''
def fibonacci_recursion(n):
    '''FibonacciRecursion'''
    if not n:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
print(fibonacci_recursion(int(input())))
