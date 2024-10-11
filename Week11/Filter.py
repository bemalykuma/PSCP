'''Filter'''
import json
def filter_id(id_score, score):
    '''Filter'''
    ans = dict(id_score)
    for i in id_score.keys():
        if id_score[i] < score:
            ans.pop(i)
    for i in sorted(ans):
        print(f"{i}\t{ans[i]:.02f}")
    if not ans:
        print("Nope")
filter_id(json.loads(input()), float(input()))
