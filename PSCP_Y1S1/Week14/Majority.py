'''Majority'''
def majority(head, vote_num):
    '''Majority'''
    dict_head = dict.fromkeys(list(i for i in range(1, head+1)),0)
    for _ in range(vote_num):
        vote = int(input())
        dict_head[vote] += 1
    high_score = max(dict_head.values())
    for i in dict_head.items():
        if i[1] == high_score:
            win = i[0]
            break
    if high_score <= (vote_num/2):
        win = 0
    print(win, high_score)
majority(int(input()), int(input()))
