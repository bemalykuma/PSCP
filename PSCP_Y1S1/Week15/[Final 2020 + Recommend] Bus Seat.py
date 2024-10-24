'''[Final 2020 + Recommend] Bus Seat'''
def bus(column, row, nai_kor):
    '''Bus seat'''
    for i in range(column, 0, -1):
        temp = i
        if i == nai_kor:
            print("XX" , end = " ")
        else:
            print(f"{i:02d}", end = " ")
        for _ in range(row-1):
            temp += column
            if temp == nai_kor:
                print("XX" , end = " ")
            else:
                print(f"{temp:02d}" , end = " ")
        if i % 2 and i != 1:
            print()
        print()
bus(int(input()), int(input()), int(input()))
