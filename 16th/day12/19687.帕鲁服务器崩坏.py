# 以下6行代码通过80%的测试用例，可以了
# n = int(input())
# s = input()
# m = int(input())

# for _ in range(m):
#     l, r = map(int, input().split())
#     print(s[l-1:r].replace("11", "1").count("10"))

# 没通过的测试样例是一个n=200000, m=200000的测试
# 样例下载下来测试了一下，光print输出这个200000行的数据就得好几分钟了，别说计算了
# 应该想想怎么样优化一下,改用sys.stdout.write试下
# import sys

# n = int(input())
# s = input()
# m = int(input())
# output = []

# for _ in range(m):
#     l, r = map(int, input().split())
#     # print(s[l-1:r].replace("11", "1").count("10"))
#     output.append(str(s[l-1:r].replace("11", "1").count("10")))

# sys.stdout.write("\n".join(output) + "\n")
# 还是没有通过，下面是可以通过全部测试样例的参考代码：
import os
import sys

n = int(input())
s = list(input())
m = int(input())
qu = [0]*n
for i in range(1,n):
    if int(s[i]) == 0 and int(s[i-1]) == 1:
        qu[i] = 1+qu[i-1]
    else:
        qu[i] = qu[i-1]       

for i in range(m):
    l,r = map(int,input().split())
    l = max(l-1,0)
    r = min(n-1,r-1)
    print(qu[r]-qu[l])


# 思路：空间换时间，新建一个和s长度一样长的列表retimes，里面存储到s的每个位置上已经重启的次数
# 然后求某个区间上重启的次数时只需要retimes[r]-retime[l]就可以了
# 似乎题目给的l, r两个参数，就暗示需要这样做了，再一看n最大取得是2*10**5，就可以确信是需要这样做的