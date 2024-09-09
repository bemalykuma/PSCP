"""ProgressiveTax"""
def main(income):
    """ProgressiveTax"""
    pay = 0
    if income > 4000000:
        money = income - 4000000
        pay += (money * 0.35) + (2000000 * 0.30) + (1000000 * 0.25) + (250000 * 0.20) \
            + (250000 * 0.15) + (200000 * 0.10) + (150000 * 0.05)
    elif 2000000 < income <= 4000000:
        money = income - 2000000
        pay += (money * 0.30) + (1000000 * 0.25) + (250000 * 0.20) + (250000 * 0.15) \
            + (200000 * 0.10) + (150000 * 0.05)
    elif 1000000 < income <= 2000000:
        money = income - 1000000
        pay += (money * 0.25) + (250000 * 0.20) + (250000 * 0.15) + (200000 * 0.10) \
            + (150000 * 0.05)
    elif 750000 < income <= 1000000:
        money = income - 750000
        pay += (money * 0.20) + (250000 * 0.15) + (200000 * 0.10) + (150000 * 0.05)
    elif 500000 < income <= 750000:
        money = income - 500000
        pay += (money * 0.15) + (200000 * 0.10) + (150000 * 0.05)
    elif 300000 < income <= 500000:
        money = income - 300000
        pay += (money * 0.1) + (150000 * 0.05)
    elif 150000 < income <= 300000:
        money = income - 150000
        pay += money * 0.05
    elif income <= 150000:
        pay += 0
    print(int(pay))
main(int(input()))
