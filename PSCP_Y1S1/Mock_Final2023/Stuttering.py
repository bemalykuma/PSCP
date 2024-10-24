'''Stuttering'''
def stuttering(word):
    '''Stuttering'''
    ans = []
    lenght = len(word)
    for i in range(1,lenght):
        if word[i] != word[i-1]:
            ans.append(word[i])
    print(word[0], " ".join(ans))
stuttering(input().split())
