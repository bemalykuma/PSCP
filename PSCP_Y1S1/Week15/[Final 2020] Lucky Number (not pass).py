'''[Final 2020] Lucky Number'''
def lucky_number(num):
    '''[Final 2020] Lucky Number'''
    num_two = list(i for i in range(1,num+1,2))
    num_three = list(num_two[i-1] for i in range(1,len(num_two)+1) if i % 3)
    num_seven = list(num_three[i-1] for i in range(1,len(num_three)+1) if i % 7)
    ans = (list(num_seven[i-1] for i in range(1,len(num_seven)+1) if i % 9) if\
         len(num_seven) >= 9 else num_seven)
    print(" ".join(str(i) for i in ans))
lucky_number(int(input()))
