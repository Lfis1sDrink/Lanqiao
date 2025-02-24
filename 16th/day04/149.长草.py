# 自己想的算法，通过循环嵌套和标记来长草，可以通过80%的测试用例，有一个Time Limit Exceeded(TLE)
# 2<= n,m <=1000, 1<= k <=1000

# 3行输入
n,m = map(int, input().split())
ground = [list(input()) for _ in range(n)]
times = int(input())


# 坐标delta
# (-1,-1)(-1, 0)(-1, 1)
# ( 0,-1)( 0, 0)( 0, 1)
# ( 1,-1)( 1, 0)( 1, 1)

for time in range(times):
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'g':
                #挨个扫描，可以长草的地方标志为o
                #注意不能直接修改成g，否则会导致下次长草的依据错乱
                if(0<= i-1 <n and ground[i-1][j] == '.'):
                    ground[i-1][j] = 'o'
                if(0<= i+1 <n and ground[i+1][j] == '.'):
                    ground[i+1][j] = 'o'
                if(0<= j-1 <m and ground[i][j-1] == '.'):
                    ground[i][j-1] = 'o'
                if(0<= j+1 <m and ground[i][j+1] == '.'):
                    ground[i][j+1] = 'o'
    #进行下一次扫描前把o的位置都长出草
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'o':
                ground[i][j] = 'g'

for i in range(n):
    for j in range(m):
        print(ground[i][j],end="")
    print()
