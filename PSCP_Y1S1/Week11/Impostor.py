'''ඞ Impostor ඞ'''
import json
def among_us():
    '''ඞ find dead and alive ඞ'''
    remains, dead_set, member_dict = 0, set(), {}
    member = input()
    if member != 'Start':
        member_dict = json.loads(member)
    while member != "Start":
        member_dict.update(json.loads(member))
        member = input()
    kicks = input()
    while kicks != "End":
        dead_set.add(kicks)
        kicks = input()
    alive_set = set(member_dict) - dead_set
    for i in alive_set:
        if member_dict[i] == "Impostor":
            remains += 1
    print(f"{remains} Impostor Remains")
    print("***Alive***")
    for i in sorted(alive_set):
        print(i,":",member_dict[i])
    print("***Dead***")
    for i in sorted(dead_set):
        print(i,":",member_dict[i])
among_us()
