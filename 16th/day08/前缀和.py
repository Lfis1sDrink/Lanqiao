'''
利用前缀和可以快速求出一段区间的和：
一段区间的和 = 右端点的前缀和 - 左端点-1的前缀和
'''
a = [1,2,3,4,5]

#前缀和Presum
def get_presum(a):
    n = len(a)
    sum = [0] * n
    sum[0] = a[0]
    for i in range(1,n):
        sum[i] = sum[i-1] +a[i]
    return sum

#O(1)的时间内求区间的和 = 右端点的前缀和 - 左端点-1的前缀和
def get_rangesum(presum, l, r):
    if l == 0:
        return presum[r]
    elif l > r:
        return -1
    else:
        return presum[r] - presum[l-1]

#a = [1,2,3,4,5]
print(get_rangesum(get_presum(a), 1,1))