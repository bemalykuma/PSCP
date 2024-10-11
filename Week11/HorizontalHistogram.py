'''HorizontalHistogram'''
def horizontal(text):
    '''HorizontalHistogram'''
    sort_ = sorted(list(i for i in text))
    low = list(i for i in sort_ if i.islower())
    up = list(i for i in sort_ if i.isupper())
    count_dict = dict.fromkeys(low+up, 0)
    ans, j = '', 1
    for i in sort_:
        count_dict[i] += 1
    for i in count_dict:
        count_dict[i] = count_dict[i] * "-"
        if len(count_dict[i]) > 5:
            while ans.count("-") < len(count_dict[i]):
                if not j % 6:
                    ans += "|"
                else:
                    ans += "-"
                j += 1
            count_dict[i] = count_dict[i].replace(count_dict[i],ans)
            ans, j = '', 1
    for x, y in count_dict.items():
        print(x, ":", y)
horizontal(input())
