import os
import sys

# 请在此输入您的代码
def input_list():
    return list(map(int, input().split()))

n,m = input_list()
a = []
b = [[0]*m for _ in range(n)]

for _ in range(n):
    a.append(input_list())

# (-1,-1)(-1, 0)(-1, 1)
# ( 0,-1)( 0, 0)( 0, 1)
# ( 1,-1)( 1, 0)( 1, 1)

delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            b[i][j] = 9
        else:
            a[i][j] == 0
            for k in range(8):
                x,y = i+delta[k][0], j + delta[k][1]
                if 0 <= x < n and 0 <= y < m:
                    b[i][j] += a[x][y]
        print(b[i][j], end=' ')
    print()




