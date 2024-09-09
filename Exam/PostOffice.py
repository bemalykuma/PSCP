"""Post Office"""
def weight_envelop(n):
    """Rate weight of envelop"""
    if 0 <= n <= 10:
        ans = 16
    elif 10 < n <= 20:
        ans = 18
    elif 20 < n <= 100:
        ans = 23
    elif 100 < n <= 250:
        ans = 28
    elif 250 < n <= 500:
        ans = 33
    elif 500 < n <= 1000:
        ans = 48
    elif 1000 < n <= 2000:
        ans = 68
    else:
        ans = 0
    return ans

def weight_package(n):
    """Rate Weight of package"""
    if 0 <= n <= 500:
        ans = 45
    elif 500 < n <= 1000:
        ans = 55
    elif 1000 < n <= 2000:
        ans = 70
    else:
        ans = 0
    return ans

def post(envelop, package):
    """Post office"""
    tax_envelop = envelop * 13
    tax_package = package * 15
    weight_e = 0
    weight_p = 0
    pay_envelop = 0
    pay_package = 0
    for _ in range(envelop):
        weight_e = float(input())
        pay_envelop += weight_envelop(weight_e)
    for _ in range(package):
        weight_p = float(input())
        pay_package += weight_package(weight_p)
    print(pay_envelop + tax_envelop + pay_package + tax_package)
post(int(input()),int(input()))
