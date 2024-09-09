"""DataSpike"""
def main(num1,num2):
    """DataSpike"""
    num3=int(input())
    num4=int(input())
    num5=int(input())
    num6=int(input())
    num7=int(input())
    num8=int(input())
    _mx=0
    if num1 > num2:
        _mx = num1
    else:
        _mx = num2
    if num3 > _mx:
        _mx = num3
    if num4 > _mx:
        _mx = num4
    if num5 > _mx:
        _mx = num5
    if num6 > _mx:
        _mx = num6
    if num7 > _mx:
        _mx = num7
    if num8 > _mx:
        _mx = num8
    print(_mx)
main(int(input()),int(input()))
