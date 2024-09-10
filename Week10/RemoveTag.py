'''Remove tag'''
def tag(html):
    '''Remove tag of html'''
    ans = ''
    i = 0
    while i < len(html):
        if html[i] == "<":
            while html[i] != ">":
                ans += html[i].replace(html[i], "")
                i += 1
            ans += " "
            i += 1
        else:
            ans += html[i]
            i += 1
    print(ans.split())
tag(input())
