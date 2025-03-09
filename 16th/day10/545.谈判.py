""""
# 题目描述

在很久很久以前，有 n 个部落居住在平原上，依次编号为 1 到 n。第 i 个部落的人数为 t_i。

有一年发生了灾荒。年轻的政治家小蓝想要说服所有部落一同应对灾荒，他能通过谈判来说服部落进行联合。

每次谈判，小蓝只能邀请两个部落参加，花费的金币数量为两个部落的人数之和，谈判的效果是两个部落联合成一个部落（人数为原来两个部落的人数之和）。

## 输入描述

输入的第一行包含一个整数 n，表示部落的数量。

第二行包含 n 个正整数，依次表示每个部落的人数。

其中，  
1 ≤ n ≤ 1000，  
1 ≤ t_i ≤ 10^4。
"""

# 堆的使用；和构造哈夫曼树类似的思想
import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)

ans = 0
while len(a) >= 2:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, x + y)
    ans += x+y

print(ans)