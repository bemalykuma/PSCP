'''MissingCard No Set'''
def missing():
    '''MissingCard No Set'''
    num, all_card, card = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"], [], "SHDC"
    length_c = len(card)
    for i in range(length_c):
        for j in num:
            all_card.append(j+card[i])
    for i in range(51):
        all_card.remove(input())
    print("".join(all_card))
missing()
