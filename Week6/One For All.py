"""One For All My Hero"""
def one_for_all(age):
    """one for all"""
    result = ""
    for i in range(1,age+1):
        char = input()
        if i == age:
            result += char + '_' + str(age)
        elif i%2:
            result += char + '*' * i
        elif not i%2:
            result += char + '-' * i
    print(result)
one_for_all(int(input()))
