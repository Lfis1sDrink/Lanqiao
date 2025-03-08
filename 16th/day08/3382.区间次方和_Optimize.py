"""
题目描述：
给定一个长度为 `n` 的整数数组 `a` 以及 `m` 个查询。
每个查询包含三个整数 `l`、`r`、`k`，表示询问区间 `[l, r]` 之间所有元素的 `k` 次方和。
请对每个查询输出一个答案，答案对 `10^9 + 7` 取模。
"""
from itertools import accumulate
import random
import sys

input = sys.stdin.readline

MOD = 10**9+7

def get_presum(needalist):
    a = needalist
    presum = list(accumulate(a))
    presum = [x % MOD for x in presum]
    return presum

def rangesum(needapresum, l, r):
    a = needapresum
    if l == 0:
        return a[r]
    else:
        return (a[r]-a[l-1] + MOD)%MOD
    
a = [1,2,3,4,5,6,7,8,9]

#原列表：a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#前缀和：p = [1, 3, 6, 10, 15, 21, 28, 36, 45]
#利用前缀和可以很快的求出原列表中某一区间的和

n,m = map(int, input().split())
# a = list(map(int, input().split()))
# 自己造个随机数列表Debug一下看看
a = [random.randint(-998399, 99328999) for _ in range(5)]

kth_powers_of_a = []

for k in range(1,6):
    temp_list = [x**k for x in a]
    kth_powers_of_a.append(get_presum(temp_list))

for _ in range(m):
    l,r,k = map(int, input().split())
    l -= 1
    r -= 1
    print(rangesum(kth_powers_of_a[k-1],l,r))