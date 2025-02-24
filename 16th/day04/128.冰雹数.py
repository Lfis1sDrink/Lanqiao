# 题目意思是不大于N的数中所有数的冰雹数中最大的数。
import time


i = int(input())
count = 0
max_num = i

# #朴素算法，直接模拟题意。计算100000大约10s
# for n in range(2,i+1):
#     while(True):
#         if(n % 2 == 0):
#             n = int(n/2)
#             if max_num < n :
#                 max_num = n
#             count+=1
#             # print(n)
#             continue
#         if(n % 2 != 0 and n != 1):
#             n = int(n*3 +1)
#             if max_num < n :
#                 max_num = n
#             count+=1
#             # print(n)
#             continue
#         if n == 1:
#             break

# 记录程序开始的时间
start_time = time.time()
#优化01，减少判断次数,程序运行时间: 8.35 秒
#优化02，删掉count+=1,程序运行时间: 6.35 秒
#优化03，使用//而不是int(),程序运行时间: 3.84 秒
#优化04，减少没用的循环，x当循环变量，
#       if x < i break 程序运行时间: 0.33 秒
#       8.35->0.33; 快27倍！
#分析: 如果x<i,那无论如何也达不到比之前的数字更大的冰雹数了
#因此没必要循环了，不用跳了直接break，找比已经算过的数大的数来算冰雹数
#总结：对于求最大的或最小的数，是否可以都按照这个思路来优化？
for n in range(2,i+1):
    x=n
    while(x != 1):
        if(x % 2 == 0):
            x = x//2
            continue
        else:
            x = x*3 +1
        if max_num < x :
            max_num = x
        #关键一句
        if x<i:
            break

# print()
print(max_num)


# 记录程序结束的时间
end_time = time.time()

# 输出运行时间
print(f"程序运行时间: {end_time - start_time} 秒")