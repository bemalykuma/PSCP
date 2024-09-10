"""Century"""
def century_trans(century_):
    """A.D. to century"""
    ans = ""
    century_ = str(century_)
    century_length = len(century_)
    century_back = int(century_[century_length-2:])
    if 1 <= century_length <=2:
        ans = 1
    elif not century_back:
        ans = century_[:century_length-2]
    else:
        ans = str(int(century_[:century_length-2])+1)
    return ans

def century(num):
    """century"""
    ans = "ERROR"
    for _ in range(num):
        year = input()
        if year[:4] == "B.E.":
            year_num = int(year[5:])
            anno_domini = year_num - 543
            if anno_domini >= 1:
                ans = century_trans(anno_domini)
            else:
                ans = "ERROR"
        elif year[:4] == "A.D.":
            anno_domini = int(year[5:])
            if anno_domini >= 1:
                ans = century_trans(anno_domini)
            else:
                ans = "ERROR"
        print(ans)
century(int(input()))
