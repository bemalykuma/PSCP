"""SaintSeiya"""
def punch(sec, rolling):
    """SaintSeiya"""
    punch_count = 0
    punch_normal = 0
    sec_count = 0
    for i in range(2,sec+1,2):
        if punch_count >= rolling:
            break
        if not i % 6:
            punch_count += 1
        elif not i % 2:
            punch_count += 165
        sec_count += 2
    if punch_count >= rolling:
        punch_normal = (sec - sec_count - 1) * 12
        if punch_normal < 0:
            punch_normal = 0
    print(punch_count + punch_normal)
punch(int(input()), int(input()))
