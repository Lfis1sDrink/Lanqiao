def input_list():
    return list(map(int, input().split()))

n,m = input_list()

spiral = [[0]*m for _ in range(n)]
tag = [[0]*m for _ in range(n)]


#走过的都置1，遇到1换方向
i,x,y = 1,0,0
while True:
    #right
    while(y+1 < m and tag[x][y+1] != 1):
        spiral[x][y] = i
        i += 1
        tag[x][y] = 1
        y += 1
    #down
    while(x+1 < n and tag[x+1][y] != 1):
        spiral[x][y] = i
        i += 1
        tag[x][y] = 1
        x += 1
    #left
    while(y-1 > -1 and tag[x][y-1] != 1):
        spiral[x][y] = i
        i += 1
        tag[x][y] = 1
        y -= 1
    #up
    while(x-1 > -1 and tag[x-1][y] != 1):
        spiral[x][y] = i
        i += 1
        tag[x][y] = 1
        x -= 1
    if(tag[x][y] == 0 and (tag[x-1][y-1]+tag[x-1][y]+tag[x-1][y+1]+tag[x][y-1]+
                            tag[x][y+1]+tag[x+1][y-1]+tag[x+1][y]+tag[x+1][y+1]) == 8):
        spiral[x][y] = i
        tag[x][y] = 1
        break


r,c = input_list()
print(spiral[r-1][c-1])

"""
#走过的都置1，遇到1换方向
转向的点交给下一步的方向判断，不然可能会越界

# (-1,-1)(-1, 0)(-1, 1)
# ( 0,-1)( 0, 0)( 0, 1)
# ( 1,-1)( 1, 0)( 1, 1)
"""

