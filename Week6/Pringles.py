"""Pringles"""
def pringles(low_1,lay,low_2,finger):
    """pick lay"""
    area = lay[:-1]
    length_area = len(lay)-1
    if finger >= length_area:
        count = area.count(")")
        ans = "None."
        area = lay.replace(")"," ")
    elif not lay.count(")"):
        count = 0
        ans = "None."
        area = lay
    else:
        if ")" in area[:finger]:
            count = area[:finger].count(")")
            area = lay[:finger].replace(")"," ") + lay[finger:]
            if ")" in lay[finger:]:
                ans = "There are still some left."
            else:
                ans = "None."
        else:
            count = 0
            ans = "There are still some left."
            area = lay
    print(count)
    print(ans)
    print(low_1)
    print(area)
    print(low_2)
pringles(input(),input(),input(),int(input()))
