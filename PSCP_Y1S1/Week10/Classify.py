'''Classify'''
def classify():
    '''Classify'''
    tmp = []
    id_ = []
    only_one = []
    count_ = []
    id_student = input()
    while id_student != "END":
        tmp.append(int(id_student[:2]))
        tmp.append(int(id_student[2:4]))
        id_.append(tmp)
        tmp = []
        id_student = input()
    id_.sort()
    for i in id_:
        if not i in only_one:
            only_one.append(i)
    for i in only_one:
        tmp += i
        tmp += str(id_.count(i))
        count_.append(tmp)
        tmp = []
    length = len(only_one)
    for i in range(length):
        if only_one[i][0] == only_one[i-1][0]:
            if not i:
                count_[i][0] = str(count_[i][0])
            else:
                count_[i][0] = "--"
        else:
            count_[i][0] = str(count_[i][0])
        count_[i][1] = str(count_[i][1])
    for i in count_:
        i = " ".join(i)
        print(i)
classify()
