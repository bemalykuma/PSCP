'''[Recommend] MultiplyMatrixPQR'''
def matrix(p, q, r):
    '''MultiplyMatrixPQR'''
    matrix_1, matrix_2 = [], []
    ans = [[0] * r for _ in range(p)]
    for _ in range(p):
        temp = []
        for _ in range(q):
            mem = int(input())
            temp.append(mem)
        matrix_1.append(temp)
    for _ in range(q):
        temp = []
        for _ in range(r):
            mem = int(input())
            temp.append(mem)
        matrix_2.append(temp)
    for i in range(p):
        for j in range(r):
            total = 0
            for k in range(q):
                total += matrix_1[i][k] * matrix_2[k][j]
            ans[i][j] = total
    for row in ans:
        print(' '.join(map(str , row)))
matrix(int(input()), int(input()), int(input()))
