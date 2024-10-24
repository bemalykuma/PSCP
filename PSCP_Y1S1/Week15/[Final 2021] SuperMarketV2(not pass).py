'''[Final 2021] SuperMarketV2'''
from math import floor
def super_market(product, total_pro, reduce_pro, sticker):
    '''SuperMarketV2'''
    price_per_product = [int(input()) for _ in range(product)]
    reduce_sticker = [i*(sticker/100) for i in price_per_product]
    reduce_sticker = (max(reduce_sticker) if reduce_sticker else 0)
    total = sum(price_per_product) - reduce_sticker
    if total >= total_pro:
        print(floor(total - total*(reduce_pro/100)))
    else:
        print(floor(total))
super_market(int(input()), int(input()), int(input()), int(input()))
