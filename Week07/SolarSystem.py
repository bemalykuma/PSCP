'''Solar System'''
def solar_system(solar):
    '''Solar System'''
    find_sun = solar.find(" sun ")
    if find_sun == -1:
        find_sun = solar.find("sun ")
        if find_sun == -1:
            find_sun = len(solar)-3
        else:
            find_sun = 0
    i = 0
    ans = ""
    result = ""
    if solar[find_sun-1].isalpha():
        for i in range(find_sun-1,-1,-1):
            if solar[i].isalpha():
                ans += solar[i]
            else:
                break
        result += ans[::-1]
        ans = ""
    if solar[find_sun+4].isalpha():
        for i in range(find_sun+5,len(solar),1):
            if solar[i].isalpha():
                ans += solar[i]
            else:
                break
        result += ans
    print(result)
solar_system(input())
