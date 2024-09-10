"""GraderMachine"""
def main(start,num):
    """Gradermachine"""
    result = 0
    pass_ = ""
    if num > start:
        for i in range(start,num+1):
            if not i % 2:
                result += i
                i = str(i)
                pass_ += " "
                pass_ += i
            else:
                result += 0
    else:
        for i in range(start,num-1,-1):
            if not i % 2:
                result += i
                i = str(i)
                pass_ += " "
                pass_ += i
            else:
                result += 0
    print(f"pass :{pass_}")
    print(f"Sum : {result}")
main(int(input()),int(input()))
