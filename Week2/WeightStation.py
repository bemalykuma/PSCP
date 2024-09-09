"""WeightStation"""
def main(a,w1,w2,w3):
    """WeightStation"""
    w4=4*a-(w1+w2+w3)
    tan=(w1+w2+w3+w4)/1000
    half=a/2
    if tan<=15:
        if abs(w1-a)<=half and abs(w2-a)<=half and abs(w3-a)<=half and abs(w4-a)<=half:
            print(f"Pass {w4:.2f}")
        else:
            print("Unbalance")
    else:
        print("Overweight")
main(float(input()),float(input()),float(input()),float(input()))
