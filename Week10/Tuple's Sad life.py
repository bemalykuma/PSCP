'''Tuple's Sad life'''
def sad(text, find_):
    '''Tuple's Sad life'''
    text = text.split()
    find_text = text.index(find_)
    count_ = text.count(find_)
    for _ in range(count_):
        for _ in range(count_):
            print(find_text,end=' ')
        print()
sad(input(), input())
