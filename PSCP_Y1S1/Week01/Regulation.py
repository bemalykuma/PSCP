"""Regulation"""
def main(a,b,c):
    """Regulation"""
    print(f"{a:>30}")
    if a>=0:
        print(f"{a:>030}")
    else:
        a=abs(a)
        print(f"-{a:>029}")
    print(f"{b:.2f}")
    print(f"{b:.12f}")
    print(f"{c:>40}")
main(int(input()),float(input()),str(input()))
