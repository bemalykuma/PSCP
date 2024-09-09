"""Sequence II"""
def main(num):
    """Sequence II"""
    result = ""
    ans = 0
    for i in range (1,num+num):
        if i % 2:
            ans = ans+i
            result += str(ans)
            result += " "
    length = len(result)
    print(result[0:length-1])
main(int(input()))
