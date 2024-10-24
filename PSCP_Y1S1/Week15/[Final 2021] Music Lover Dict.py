'''[Final 2021] Music Lover'''
def music_lover(artist):
    '''[Final 2021] Music Lover'''
    artist_music = [input().strip().split("-") for _ in range(artist)]
    dict_ans = {}
    length = len(artist_music)
    for i in range(length):
        if artist_music[i][0] in dict_ans:
            dict_ans[artist_music[i][0]] += [artist_music[i][1]]
        else:
            dict_ans[artist_music[i][0]] = [artist_music[i][1]]
    for i, j in dict_ans.items():
        print(i)
        print(*j, sep="\n")
music_lover(int(input()))
