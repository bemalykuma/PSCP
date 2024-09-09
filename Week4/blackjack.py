"""Blackjack"""
def main(num):
    """Blackjack"""
    def card(c):
        if c in ("J" ,"Q" ,"K"):
            c = 10
        return c
    result = 0
    count = 0
    for _ in range(num):
        item = card(str(input()))
        if item == "A":
            count += 1
            result += 0
        else:
            item = int(item)
            result += item
    if num == 2 and count == 2:
        ans = 12
    elif result + ( count * 11 ) <= 21:
        ans = result + ( count * 11 )
    else:
        if count == 1:
            ans = result + count
        elif count > 1 and result < 10:
            ans = result + 11 + ( count - 1 )
        else:
            ans = result + count
    print(ans)
main(int(input()))
