'''BloodDonation'''
def blood(age, weight, count_blood):
    '''BloodDonation'''
    con_to_no , ans = weight < 45 or (not count_blood and age >= 55), "No"
    if age == 17 or 60 <= age <= 70:
        if input() == "True" and not con_to_no:
            ans = "Yes"
    if 17 < age < 60 and not con_to_no:
        ans = "Yes"
    print(ans)
blood(int(input()), int(input()), int(input()))
