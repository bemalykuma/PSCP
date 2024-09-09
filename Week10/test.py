ls = []
temp = []
tmp = 0
ans = []
num = int(input())
for i in range(num):
    n = int(input())
    for i in range(n):
        pos = input()
        ls.append(pos)
        ls.append(ls[0][-1])
        pos = pos.split()
        for i in pos:
            tmp += int(i)
        ls.append(tmp)
        temp.append(ls)
        ls = []
        tmp = 0
    ans.append(temp)
    temp = []
def sumary(s):
    return s[2]
def y(s):
    return s[1]
a = []
oo = 0
for i in ans:
    i.sort(key=sumary)
    temp.append(i)
    for j in i:
        if oo == len(i) - 1:
            break
        if i[oo][2] == i[oo+1][2]:
            a.append(i[oo])
            if not i[oo+1] in a:
                a.append(i[oo+1])
        oo += 1
    a.sort(reverse=True, key=y)
print(a)
print(temp)
print(ans)