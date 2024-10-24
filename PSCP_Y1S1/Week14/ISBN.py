'''ISBN'''
def pokemon(isbn):
    '''ISBN'''
    for i in isbn:
        if i.isalpha():
            isbn = isbn.replace(i,"")
    mul_2 = list(int(i) for i in isbn)
    mul_1 = list(range(len(isbn), 1, -1))
    length = len(mul_1)
    summary = 0
    for i in range(length):
        summary += mul_1[i] * (mul_2[:-1])[i]
    isbn_cal = -summary % 11
    if isbn_cal == mul_2[-1]:
        print("Yes")
        return
    if isbn_cal > 9:
        isbn_cal = "X"
    print(f"No {isbn_cal}")
pokemon(input().replace("-",""))
