"""Lift"""
def lift(num, weight_lift):
    """Lift"""
    all_weight = 0
    ans = "Not Safe"
    for _ in range(num):
        age = int(input())
        weight = float(input())
        all_weight += weight
        if age >= 12:
            ans = "Safe"
        if all_weight > weight_lift:
            ans = "Not Safe"
    if not num:
        ans = "Safe"
    print(ans)
lift(int(input()), float(input()))
