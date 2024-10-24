"""PrasomSib"""
def sib(number):
    """sib"""
    count = 0
    for i,n in enumerate(number): 
        total = int(n)
        for n2 in number[i+1:]:
            total += int(n2)
            if total == 10:
                count += 1
            elif total > 10:
                break
    print(count)
sib(input())
