"""Turnstile"""
def turnstile(action):
    """Turnstile"""
    count = 0
    result = ""
    while action != "END":
        result += action
        if "CP" in result:
            count += 1
            result = ""
        action = input()
    print(count)
turnstile(input())
