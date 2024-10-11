'''Roman'''
def roman(num):
    '''Roman'''
    roman_i = {'I': 1,'IV': 4,'V' : 5,'IX' : 9,'X' : 10,'XL' : 40,'IL' : 49,'L' : 50,'XC' : 90,\
               'IC' : 99,'C' : 100,'CD' : 400,'ID' : 499,'D' : 500,'CM': 900,'IM': 999,'M': 1000}
    answer, i = 0, 0
    result = ""
    while i < len(num)-1:
        result = num[i]
        if result + num[i+1] in roman_i:
            answer += roman_i[result+num[i+1]]
            i += 2
        else:
            answer += roman_i[result]
            i += 1
    print(answer)
roman(input()+" ")
