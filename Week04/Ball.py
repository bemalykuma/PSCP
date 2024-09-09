"""Ball"""
def main(num):
    """Ball"""
    count = 0
    while True:
        if (num*(3/5)) * 100 >= 1:
            count += 1
            num = num*(3/5)
        else:
            break
    print(count)
main(float(input()))
