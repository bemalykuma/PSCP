"""PH"""
def main(ph):
    """ph"""
    if 0 <= ph < 7:
        print("acidic")
    elif 7 < ph <= 14:
        print("akaline")
    elif ph == 7:
        print("neutral")
    else:
        print("error")
main(float(input()))
