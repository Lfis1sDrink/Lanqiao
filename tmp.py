# n,m = map(int, input().split())
# opt = []
# goodsList = [0]*(n+1)

# # 存储每个操作，同时对goodsList应用差分数组
# for i in range(m):
#   L,R = map(int, input().split())
#   opt.append((L,R))
#   goodsList[L-1] += 1
#   if R <= n+1:
#     goodsList[R] -= 1

# # 用前缀和得出结果数组
# for i in range(1,n+1):
#   goodsList[i] += goodsList[i-1]

# # print(goodsList)
# total0 = 0
# for i in range(len(goodsList)-1):
#   if goodsList[i] == 0:
#     total0 += 1

# for L,R in opt:
#   cnt_1 = 0
#   cnt_0 = 0
#   for i in range(L-1,R):
#     if goodsList[i] == 1:
#       cnt_1 += 1
#     if goodsList[i] == 0:
#       cnt_0 += 1
#   print(total0 - cnt_0 + cnt_1)
  


class Data:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return other.num + self.num > self.num + other.num


n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append(Data(bin(i)[2:]))
arr.sort(reverse=True)
ans = ""
for i in range(len(arr)):
    ans += arr[i].num
print(int("0b" + ans, 2))
