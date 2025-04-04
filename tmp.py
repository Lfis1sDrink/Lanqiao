from time import sleep

n, m = map(int, input().split())
ops = []
diff = [0] * (n + 2)  # 差分数组，处理1-based到n-based的区间

for _ in range(m):
    L, R = map(int, input().split())
    ops.append((L, R))
    diff[L] += 1
    if R + 1 <= n:
        diff[R + 1] -= 1

# 计算总库存量数组
total = [0] * (n + 1)  # 1-based索引
current = 0
for i in range(1, n + 1):
    current += diff[i]
    total[i] = current

# 构建前缀和数组，统计0和1的出现次数
prefix_0 = [0] * (n + 1)
prefix_1 = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_0[i] = prefix_0[i-1] + (1 if total[i] == 0 else 0)
    prefix_1[i] = prefix_1[i-1] + (1 if total[i] == 1 else 0)

total_zero = prefix_0[n]  # 整个数组中的0的总数

for L, R in ops:
    # 区间内等于1的数目
    A = prefix_1[R] - prefix_1[L-1]
    # 区间外的0数目 = 总0数目 - 区间内的0数目
    zero_in = prefix_0[R] - prefix_0[L-1]
    B = total_zero - zero_in
    print(A + B)