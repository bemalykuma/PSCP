"""Calculator"""
def cal(last_num):
    """Calculator"""
    result = ""
    count = 0
    for i in range(1,last_num+1):
        if i == last_num:
            result += str(i) + "="
            break
        result += str(i) + "+"
    count = len(result)
    if last_num == 1:
        count = 1
    print(count)
cal(int(input()))
