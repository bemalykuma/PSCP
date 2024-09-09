"""SecondConverter"""
def main(k,s,m,h):
    """SecondConverter"""
    sec = k % s
    min_ = k//s
    hour = min_//m
    min_ %= m
    hour %= h
    if hour > h:
        hour %= h
    print(f"{hour}:{min_}:{sec}")
main(int(input()),int(input()),int(input()),int(input()))
