"""HowLong"""
def main(num):
    """HowLong"""
    result = 0
    for _ in num:
        result += 1
    if int(num) < 0:
        result -= 1
    print(result)
main(str(input()))
