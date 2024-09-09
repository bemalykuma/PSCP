"""SumOfNumber"""
def main(want):
    """SumOfNumber"""
    result = 0
    while True:
        num = int(input())
        result += num
        if num == -1 or result == want:
            if num == -1:
                result += 1
            break
    print(result)
main(int(input()))
