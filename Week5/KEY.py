"""Key"""
def main(id_card):
    """key"""
    result = 0
    for i in id_card:
        result += int(i)
    digits_3 = int(id_card[10:]) * 10
    key = result + digits_3
    if key >= 10000:
        key = str(key)[1:]
    elif key < 1000:
        key += 1000
    print(key)
main(input())
