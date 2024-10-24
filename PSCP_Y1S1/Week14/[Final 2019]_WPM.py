'''WPM'''
def for_kids(r):
    '''WPM for kids'''
    if r < 11:
        return "Very Slow"
    if 11 <= r <= 20:
        return "Slow"
    if 21 <= r <= 30:
        return "Average"
    if 31 <= r <= 40:
        return "Fast"
    return "Very Fast"

def for_adults(r):
    '''WPM for Adults'''
    if r < 26:
        return "Very Slow"
    if 26 <= r <= 35:
        return "Slow/Beginner"
    if 36 <= r <= 45:
        return "Intermediate/Average"
    if 46 <= r <= 65:
        return "Fast/Advanced"
    if 65 <= r <= 80:
        return "Very Fast"
    return "Insane"

def wpm(age, score):
    '''wpm'''
    if age == "Kids":
        print(for_kids(score))
    else:
        print(for_adults(score))
wpm(input(), int(input()))
