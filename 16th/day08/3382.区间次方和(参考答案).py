import os
import sys
from itertools import accumulate
MOD = 10 ** 9 + 7
input = sys.stdin.readline

# 请在此输入您的代码

n, m = map(int, input().split())
a = list(map(int, input().split()))

# # 第一种写法： 数据比较大的时候运行超时
# def get_presum(a):
#   n = len(a)
#   sum = [0] * n
#   sum[0] = a[0]  # 因为题中是从a[1]开始的， 我们的 a[0] 就是题目的 a[1]
#   for i in range(1, n):  # 前缀和公式： sum[i] = sum[i - 1] + a[i]  从 1 开始，因为公式中 i - 1 的原因，并且第0位已经赋值了
#     sum[i] = sum[i - 1] + a[i]
#     sum = [x % MOD for x in sum] # 保证 sum 里的每个元素小于等于 MOD 
#   return sum

# 第二种写法： 利用 itertools 中的 accumulate（）进行累积计算
def get_presum(a):
  sum = list(accumulate(a))
  sum = [x % MOD for x in sum]

  return sum 

def get_sum(sum, l, r):
  if l == 0:  # 预防范围
    return sum[r]
  else:
    return (sum[r] - sum[l - 1] + MOD) % MOD  # 里面加 MOD 是为了防止里面的数字为负数，影响取模结果

sum_list = [] 
# 存储 a 数组的前缀和的次方
for i in range(1, 6):
  tmp_a = [x ** i for x in a]
  sum_list.append(get_presum(tmp_a))  # 把1到5的次方的 sum_list 输出大概是：[[1, 3, 6, 10, 15], [1, 5, 14, 30, 55]，.....]这样


for _ in range(m):
   l, r, k = map(int, input().split())
   print(get_sum(sum_list[k - 1], l - 1, r - 1))