"""Real"""
def seven_segment():
    """7-Segment"""
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    f = input()
    g = input()
    dp = input()
    num_1 = a == "off" and b == "on" and c == "on" and d == "off" and e == "off" and\
          f == "off" and g == "off"
    num_2 = a == "on" and b == "on" and c == "off" and d == "on" and e == "on" and\
          f == "off" and g == "on"
    num_4 = a == "off" and b == "on" and c == "on" and d == "off" and e == "off" and\
          f == "on" and g == "on"
    num_7 = a == "on" and b == "on" and c == "on" and d == "off" and e == "off" and \
        f == "off" and g == "off"
    a_b_c_d = a == "on" and b == "on" and c == "on" and d == "on"
    a_c_d_not_b = a == "on" and b == "off" and c == "on" and d == "on"
    if a_b_c_d and e == "on" and f == "on" and g == "off":
        ans = "0"
    elif num_1:
        ans = "1"
    elif num_2:
        ans = "2"
    elif a_b_c_d and e == "off" and f == "off" and g == "on":
        ans = "3"
    elif num_4:
        ans = "4"
    elif a_c_d_not_b and e == "off" and f == "on" and g == "on":
        ans = "5"
    elif a_c_d_not_b and e == "on" and f == "on" and g == "on":
        ans = "6"
    elif num_7:
        ans = "7"
    elif a_b_c_d and e == "on" and f == "on" and g == "on":
        ans = "8"
    elif a_b_c_d and e == "off" and f == "on" and g == "on":
        ans = "9"
    else:
        ans = "Error"
    if dp == "on":
        ans += "."
    return ans

def real():
    """Real"""
    first = seven_segment()
    second = seven_segment()
    last = seven_segment()
    result = first +  second + last
    if result.count(".") > 1 or "Error" in result:
        print("Error")
    else:
        print(f"{float(result):.02f}")
real()
