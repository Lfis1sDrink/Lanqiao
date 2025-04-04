# # def howManyZero(aList):
# #   count = 0
# #   for _ in range(len(aList)):
# #     if aList[_] == 0:
# #       count += 1
# #   return count


# n,m = map(int, input().split())

# ml = []
# mr = []

# for _ in range(m):
#   l,r = map(int, input().split())
#   ml.append(l)
#   mr.append(r)

# # def do(alist, group):
# #   begin = ml[group]-1
# #   end = mr[group]-1
# #   for i in range(begin,end+1,1):
# #     # if i < begin:
# #     #   continue
# #     # if i > end:
# #     #   break
# #     # if begin <= i <= end:
# #       alist[i] += 1


# for i in range(m):
#   goodsList = [0]*n
#   for j in range(m):
#     if i == j:
#       continue
#     # 执行操作
#     begin = ml[j]-1
#     end = mr[j]-1
#     for x in range(begin,end+1,1):
#       goodsList[x] += 1


#   print(str(goodsList).count('0'))

# # 以上为暴力模拟的算法，但是会TLE，通过0%的测试样例
##############################################################

# from time import sleep

# n, m = map(int, input().split())
# ops = []
# diff = [0] * (n + 2)  # 差分数组，处理1-based到n-based的区间

# for _ in range(m):
#     L, R = map(int, input().split())
#     ops.append((L, R))
#     diff[L] += 1
#     if R + 1 <= n:
#         diff[R + 1] -= 1

# # 计算总库存量数组
# total = [0] * (n + 1)  # 1-based索引
# current = 0
# for i in range(1, n + 1):
#     current += diff[i]
#     total[i] = current

# # 构建前缀和数组，统计0和1的出现次数
# prefix_0 = [0] * (n + 1)
# prefix_1 = [0] * (n + 1)
# for i in range(1, n + 1):
#     prefix_0[i] = prefix_0[i-1] + (1 if total[i] == 0 else 0)
#     prefix_1[i] = prefix_1[i-1] + (1 if total[i] == 1 else 0)

# total_zero = prefix_0[n]  # 整个数组中的0的总数

# for L, R in ops:
#     # 区间内等于1的数目
#     A = prefix_1[R] - prefix_1[L-1]
#     # 区间外的0数目 = 总0数目 - 区间内的0数目
#     zero_in = prefix_0[R] - prefix_0[L-1]
#     B = total_zero - zero_in
#     print(A + B)

# DPSK给的答案，全部通过。。。
##############################################################

# 试一下把不进行某个操作转化为：所有操作都做完以后哪些商品只有1件货（也就是说它本来应该是0件货）


# n, m = map(int, input().split())
# goodsList = [0]*n

# for _ in range(m):
#   l,r = map(int, input().split())
#   for i in range(l,r+1,1):
#     goodsList[i] += 1


# 然后发现一个问题：使用print(str(goodsList).count('0'))判断的话会不会把10，20这种结果的0也统计进去，从而导致结果出错的
# 修改：

# n,m = map(int, input().split())

# ml = []
# mr = []

# for _ in range(m):
#   l,r = map(int, input().split())
#   ml.append(l)
#   mr.append(r)

# for i in range(m):
#   goodsList = [0]*n
#   for j in range(m):
#     if i == j:
#       continue
#     # 执行操作
#     begin = ml[j]-1
#     end = mr[j]-1
#     for x in range(begin,end+1,1):
#       goodsList[x] += 1
#   ans = 0
#   for _ in range(n):
#     if goodsList[_] == 0:
#       ans += 1
#   print(ans)


##############################################################

# 2025年4月4日重新做一遍

n,m = map(int, input().split())
opt = []

for i in range(m):
  L,R = map(int, input().split())
  opt.append((L,R))

for i in range(m):
  goodsList = [0]*(n+1)
  # 输出如果不执行第 i 个操作，则最终库存量为 0 的商品种类数
  # 利用差分数组更新库存
  for j in range(m):
    if j == i:#第i行不执行第i个操作
      continue
    L = opt[j][0]
    R = opt[j][1]
    goodsList[L-1] += 1
    goodsList[R] -= 1
  # 用前缀和还原数组
  for j in range(1,len(goodsList)):
    goodsList[j] += goodsList[j-1]
#   print(goodsList)
  # 输出结果
  ans = 0
  for i in range(n):
    if goodsList[i] == 0:
      ans += 1
  print(ans)
  



