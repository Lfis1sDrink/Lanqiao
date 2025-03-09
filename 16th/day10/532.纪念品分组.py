"""
# 题目描述

元旦快到了，校学生会让乐乐负责新年晚会的纪念品发放工作。为使得参加晚会的同学所获得的纪念品价值相对均衡，他要把购来的纪念品根据价格进行分组，但每组最多只能包括两件纪念品，并且每组纪念品的价格之和不能超过一个给定的整数。为了保证在尽量短的时间内发完所有纪念品，乐乐希望分组的数目最少。

你的任务是写一个程序，找出所有分组方案中分组数最少的一种，输出最少的分组数目。

## 输入描述

第 1 行包括一个整数 w (80 ≤ w ≤ 200)，为每组纪念品价格之和的上限。

第 2 行为一个整数 n (1 ≤ n ≤ 30000)，表示购来的纪念品的总件数。

第 3 ～ n+2 行每行包含一个正整数 p_i (5 ≤ p_i ≤ w)，表示所对应纪念品的价格。

## 输出描述

输出一个整数，表示最少的分组数目。

## 运行限制

最大运行时间：1s  
最大运行内存：128M

"""

# 这题目今天琢磨了很久，一度以为是题出错了。
# 想法是用堆来做匹配，一直把一部分匹配成小于等于W的组合就算分组了一次。
# 结果遇到1,1,1,1,1,1,1,1,1,1,1,99这种例子死活过不去，按照我的算法和模拟最后最少的分组应该是2组，但是答案是5组
# 非常挠头，最后怀疑是题出错了，最后最后才发现题目要求每组最多两个礼物。。
# 不过也有收获，今天学会了下载测试样例到本地，还有使用launch.json实现调试重定向
# 干饭


# 用堆实现只能通过60%的样例，其余全部TLE。
# （堆无法删除指定元素，每次删除指定元素必须遍历整个堆，因为堆是用二叉树实现的）
# import heapq

# w = int(input())
# n = int(input())
# priceList = [int(input()) for _ in range(n)]
# print("readed")
# heapq.heapify(priceList)
# print("heapq")
# result = []

# def delementOnheap(heap,target):
# # 遍历堆并删除目标元素
#     temp_heap = []
#     found = False
#     while heap:
#         min_elem = heapq.heappop(heap)
#         if min_elem == target and not found:
#             found = True
#             # print(f"找到了并移除了元素: {target}")
#             continue  # 跳过该元素
#         heapq.heappush(temp_heap, min_elem)

#     # 将剩余元素恢复回堆
#     heap = temp_heap
#     heapq.heapify(heap)
#     return heap

# while(len(priceList) >= 2):
#     min = heapq.heappop(priceList)
#     max = heapq.nlargest(1,priceList)[0]
#     priceList = delementOnheap(priceList,max)
#     if (max + min) < w:
#         heapq.heappush(priceList,min+max)
#     elif (max + min) == w:
#         result.append(max + min)
#     else:
#         result.append(max)
#         heapq.heappush(priceList,min)

# print(len(result)+1)


# 双指针实现
m = int(input())
n = int(input())
s=[int(input()) for i in range(n)]
s.sort()

l,r = 0, n-1
ans = 0
while l<=r:
    if s[l]+s[r]<=m:
        l+=1
    r-=1
    ans+=1

print(ans)