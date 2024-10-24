'''Taking Turns'''
import json
def turns(list_input):
    '''Taking Turns'''
    if list_input == "[]":
        print("[]")
        return
    use_json = json.loads(list_input)
    ans = []
    count = 0
    while use_json != []:
        if not count % 2:
            ans.append(use_json[-1])
            use_json.pop()
            if use_json == []:
                break
            ans.append(use_json[0])
            use_json.remove(use_json[0])
            count += 1
        elif count % 2:
            ans.append(use_json[0])
            use_json.remove(use_json[0])
            if use_json == []:
                break
            ans.append(use_json[-1])
            use_json.pop()
            count += 1
    print(ans)
turns(input())
