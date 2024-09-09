"""Grade III"""
def main(num):
    """Grade III"""
    result = 0
    def grade(x):
        if 95<=x<=100:
            x = 4
        elif 90<=x<95:
            x = 3.5
        elif 85<=x<90:
            x = 3
        elif 80<=x<85:
            x = 2.5
        elif 75<=x<80:
            x = 2
        elif 70<=x<75:
            x = 1.5
        elif 65<=x<70:
            x = 1
        elif 60<=x<65:
            x = 0.5
        elif 0<=x<60:
            x = 0
        return x
    for _ in range(num):
        score = grade(float(input()))
        result += score
    gpax = int((result/num)*100)
    print(f"{gpax/100:.2f}")
main(int(input()))
