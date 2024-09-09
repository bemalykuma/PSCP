"""Surprising"""
def main(a,maksud):
    """Surprising"""
    noisud = a - (maksud * 2)
    if noisud < 0:
        noisud = 0
    if maksud - noisud > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()),float(input()))
