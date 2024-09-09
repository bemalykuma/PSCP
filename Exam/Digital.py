"""Digital Wallet"""
def digital(name, thai, home, age, income):
    """digital"""
    bank = float(input())
    correct = "Yes", "True"
    check_age = age >= 16
    check_income = income <= 840000
    check_bank = bank <= 500000
    check_thai_home = thai in correct and home in correct
    if check_thai_home and check_age and check_income and check_bank:
        print(f'Congratulations! {name} is qualified to receive a digital wallet amount'\
             ' of 10,000 baht, sponsored by all taxpayers in Thailand.')
    else:
        print(f"Unfortunately, {name} is not qualified.")
digital(input(), input(), input(), float(input()), float(input()))
