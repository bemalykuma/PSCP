'''AlmostMean'''
def mean(person):
    '''AlmostMean'''
    averange = 0
    sumary = 0
    find_almost = 0
    id_score_list = []
    almost_score = []
    for _ in range(person):
        id_score = input().split()
        id_score_list.append(id_score)
        sumary += float(id_score[1])
    if person > 0:
        averange = sumary/person
    for i in id_score_list:
        if float(i[1]) <= averange:
            almost_score.append(i[1])
    for i in almost_score:
        if float(i) >= find_almost:
            find_almost = float(i)
    for i in id_score_list:
        if str(find_almost) in i:
            print('\t'.join(i))
mean(int(input()))
