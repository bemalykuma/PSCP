'''[Final 2021] Music Lover'''
def music_lover(artist):
    '''[Final 2021] Music Lover'''
    artist_music = [input().strip().split("-") for _ in range(artist)]
    list_music, mu = [], []
    for i in artist_music:
        mu.append(i)
    while artist_music:
        length = len(artist_music)
        a = artist_music[0][0]
        for i in range(length):
            if artist_music[i][0] == a:
                list_music.append(artist_music[i][1])
        print(a)
        for k in list_music:
            print(k)
        for i in mu:
            if a in i:
                artist_music.remove(i)
        list_music = []
music_lover(int(input()))
