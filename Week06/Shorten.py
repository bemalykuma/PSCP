"""Shorten"""
def shorten():
    """Shorten"""
    num = str(int(input()))
    special_char = ""
    result = num
    if num == "-1":
        result = ""
    else:
        while num != "-1":
            start = num
            num = str(int(input()))
            if int(num) - int(start) == 1:
                special_char += "-"
            if "-" in special_char:
                special_char = "-"
            if int(num) - int(start) > 1:
                if not special_char.count("-"):
                    result += ""
                else:
                    result += special_char + start
                result += ", "
                result += num
                special_char = ""
            if num == "-1":
                if not special_char.count("-"):
                    result += ""
                else:
                    result +=special_char + start
                break
        print(result)
shorten()
