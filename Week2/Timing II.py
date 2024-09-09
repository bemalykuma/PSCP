"""Timing II"""
def main(second):
    """Timing II"""
    minutes=second//60
    seconds=second%60
    hours=minutes//60
    minutes=minutes%60
    days=hours//24
    hours=hours%24
    if days<10000:
        print(f"{days:>04}:{hours:>02}:{minutes:>02}:{seconds:>02}")
    else:
        print("ERR_:__:__:__")
main(int(input()))
