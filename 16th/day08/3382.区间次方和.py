"""
题目描述：
给定一个长度为 `n` 的整数数组 `a` 以及 `m` 个查询。
每个查询包含三个整数 `l`、`r`、`k`，表示询问区间 `[l, r]` 之间所有元素的 `k` 次方和。
请对每个查询输出一个答案，答案对 `10^9 + 7` 取模。
"""
# itertools 是 Python 的一个模块，提供了用于高效循环和组合操作的函数。
# 这个名字来源于 "iterator"（迭代器）和 "tools"（工具）的组合，表示它是一个处理迭代器的工具集。
from itertools import accumulate
import sys

MOD = 10**9 + 7
input = sys.stdin.readline

def prefixsum(a):
    # sum = [0] * len(a)
    # for i in range(len(a)):
    #     sum[i] = sum[i-1] + a[i]
    # return sum
  sum=list(accumulate(a))
  sum=[i % MOD for i in sum]
  return sum


def rangesum(presum, l, r):
    if l == 0:
        return presum[r]
    else:
        return (presum[r] - presum[l-1]  + MOD) % MOD

n,m = map(int, input().split())
ak1 = list(map(int, input().split()))
# ak2 = [x**2 for x in ak1 ]
# ak3 = [x**3 for x in ak1 ]
# ak4 = [x**4 for x in ak1 ]
# ak5 = [x**5 for x in ak1 ]
# ak = [ak1,ak2,ak3,ak4,ak5]
# ak = [[x**i for x in ak1] for i in range(1, 6)]

sum_list = [] 
# 存储 a 数组的前缀和的次方
for i in range(1, 6):
  tmp_a = [x ** i for x in ak1]
  sum_list.append(prefixsum(tmp_a))  # 把1到5的次方的 sum_list 输出大概是：[[1, 3, 6, 10, 15], [1, 5, 14, 30, 55]，.....]这样


for _ in range(m):
    l,r,k = map(int, input().split())
    print(rangesum(sum_list[k-1], l-1, r-1) % MOD)


"""
Dpsk给的，结果对但是运行时间超时

MOD = 10**9 + 7

n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    l, r, k = map(int, input().split())
    l -= 1  # 转换为0-based索引
    r -= 1
    total = 0
    for i in range(l, r + 1):
        total = (total + pow(a[i], k, MOD)) % MOD
    print(total)
"""

