'''MissingCard'''
def missing():
    '''MissingCard'''
    num, card = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"], "SHDC"
    all_card, missing_card = set(), set()
    length_c = len(card)
    for i in range(length_c):
        for j in num:
            all_card.add(j+card[i])
    for i in range(51):
        missing_card.add(input())
    print("".join(all_card - missing_card))
missing()
