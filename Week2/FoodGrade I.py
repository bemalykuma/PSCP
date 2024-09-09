"""Foodgrade"""
def main(w1,w2,w3,w4,w5):
    """food"""
    def food(w):
        if 50<=w<=70:
            w=1
        else:
            w=0
        return w
    w1 = food(w1)
    w2 = food(w2)
    w3 = food(w3)
    w4 = food(w4)
    w5 = food(w5)
    def inp():
        w6 = food(int(input()))
        w7 = food(int(input()))
        w8 = food(int(input()))
        w9 = food(int(input()))
        w10 = food(int(input()))
        w11 = food(int(input()))
        w12 = food(int(input()))
        w13 = food(int(input()))
        w14 = food(int(input()))
        w15 = food(int(input()))
        w=w6+w7+w8+w9+w10+w11+w12+w13+w14+w15
        return w
    def inp2():
        w16 = food(int(input()))
        w17 = food(int(input()))
        w18 = food(int(input()))
        w19 = food(int(input()))
        w20 = food(int(input()))
        w21 = food(int(input()))
        w22 = food(int(input()))
        w23 = food(int(input()))
        w24 = food(int(input()))
        w=w16+w17+w18+w19+w20+w21+w22+w23+w24
        return w
    print(w1+w2+w3+w4+w5+inp()+inp2())
main(int(input()),int(input()),int(input()),int(input()),int(input()))
