"""ConpositeFunction"""
def main(x):
    """ConpositeFunction"""
    def f(x):
        ans=2*x
        return ans
    def g(x):
        ans=x/2+1
        return ans
    print(f"{f(g(x)):.2f}")
    print(f"{g(f(x)):.2f}")
main(int(input()))
