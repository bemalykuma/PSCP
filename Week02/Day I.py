"""Day I"""
def main(year):
    """Day I"""
    if not year%4:
        if not year%100:
            if not year%400:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
main(int(input()))
