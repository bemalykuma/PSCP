"""Rule of Three"""
def kanom(piece):
    """Rule of Three"""
    price = float(input())
    weight = float(input())
    kwhamkum = weight / price
    kum_mak = kwhamkum
    kum_price = price
    kum_weight = weight
    for _ in range(piece-1):
        price = float(input())
        weight = float(input())
        kwhamkum = weight / price
        if kwhamkum > kum_mak or kwhamkum == kum_mak and price < kum_price:
            kum_mak = kwhamkum
            kum_price = price
            kum_weight = weight
    print(f"{kum_price:.02f} {kum_weight:.02f}")
kanom(int(input()))
