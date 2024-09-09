"""Kaprekar"""
def ordinal(n):
    """highest to lowest"""
    length = len(str(n))
    ls = []
    for i in n:
        ls += i
    n = ls
    for i in range(length):
        for j in range(i+1, length):
            if n[i] >= n[j]:
                n[i], n[j] = n[j], n[i]
    return n

def kaprekar(num):
    """Kaprekar"""
    mak = ordinal(num)
    mak.reverse()
    result_mak = ""
    result_noi = ""
    count = 0
    ans = num
    while ans != 6174:
        for i in ordinal(str(ans)):
            result_noi += i
        for i in mak:
            result_mak += i
        ans = int(f"{str(int(result_mak)):<04}") - int(result_noi)
        count += 1
        result_mak = ""
        result_noi = ""
        mak = ordinal(str(ans))
        mak.reverse()
    print(count)
kaprekar(input())
 