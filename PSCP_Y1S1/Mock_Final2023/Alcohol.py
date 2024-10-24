'''Alcohol'''
def alcohol(m_f, weight, drive, cc, per):
    '''Alcohol'''
    can = int(input())
    rest = int(input())
    al = ((per * cc)/100)*can
    blood_male = al/(weight*0.68*10)
    blood_female = al/(weight*0.55*10)
    reduce = rest * 0.015
    safe_male = m_f == "Male" and blood_male-reduce <= 0.05 and drive == "Yes"
    safe_female = m_f == "Female" and blood_female-reduce <= 0.05 and drive == "Yes"
    if safe_female or safe_male:
        print("Safe")
    else:
        print("Not Safe")
alcohol(input(),float(input()),input(),float(input()),float(input()))
