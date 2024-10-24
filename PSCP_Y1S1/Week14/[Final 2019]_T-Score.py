'''[Final 2019] T-score'''
def z_score(score, average, s_d):
    '''calculate Z_Score'''
    return (score - average) / s_d

def tscore(all_student):
    '''how to calculate T-score'''
    int(input())
    list_score, list_z_score = [], []
    for _ in range(all_student):
        list_score.append(int(input()))

    sum_score = sum(list_score)
    average = sum_score / all_student
    sum_score_pow_2 = 0

    for i in list_score:
        sum_score_pow_2 += i**2

    s_d = ((all_student * sum_score_pow_2-(sum_score)**2)/(all_student*(all_student - 1)))**0.5

    for i in list_score:
        if not s_d:
            list_z_score.append(0)
        else:
            list_z_score.append(z_score(i, average, s_d))

    for i in list_z_score:
        print(f"{(50 + 10*i):.2f}")
tscore(int(input()))
