'''[Recommend] VerticalHistogram'''
def vertical(txt):
    '''VerticalHistogram'''
    alpha = []
    dict_alpha = {}
    for i in txt:
        if not i in alpha and i.isalpha():
            alpha.append(i)
            dict_alpha[i] = 1
        elif i.isalpha():
            dict_alpha[i] += 1
    alpha.sort()
    maksud = max(dict_alpha.values())
    for i in range(maksud, 0, -1):
        print(f"{i:2d}"+" ", end = "")
        for j in alpha:
            if dict_alpha[j] >= i:
                print(" *", end = '')
            else:
                print("  ", end = '')
        print()
    print("    " + " ".join(alpha))
vertical(input())
