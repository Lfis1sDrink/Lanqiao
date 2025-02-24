from collections import deque

# 3行输入
n,m = map(int, input().split())
ground = [list(input()) for _ in range(n)]
times = int(input())
dir = [(-1,0),(1,0),(0,-1),(0,1)]

queue = deque()

for i in range(n):
    for j in range(m):
        if ground[i][j] == 'g': queue.append([i,j]) 

def bfs():
    a = len(queue)
    while a > 0:
        x,y = queue.popleft()

        for u,v in dir:
            nx,ny = x+u, y+v
            if 0<= nx < n and 0<= ny <m and ground[nx][ny] == '.':
                ground[nx][ny] = 'g'
                queue.append([nx,ny])
        a -=1

for _ in range(times):
    bfs()

for i in ground:
    print("".join(i))
