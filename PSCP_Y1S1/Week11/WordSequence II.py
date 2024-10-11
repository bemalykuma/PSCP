'''WordSequence II'''
def sequence(word_1, word_2):
    '''WordSequence II'''
    if len(word_2) >= len(word_1):
        for i in range(len(word_2)+1):
            print(word_2[:i]+word_1[i:])
    else:
        for i in range(len(word_1)+1):
            print(word_2[:i]+word_1[i:])
sequence(input(), input())
