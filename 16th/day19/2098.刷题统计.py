# a,b,n = map(int, input().split())

# acc = 0
# day = 0
# i = 0
# week = [1,2,3,4,5,6,7]
# while acc < n:
#     i = (i+1) % 7
#     if week[i] <= 5:
#         acc += a
#         day += 1
#     elif week[i] > 5:
#         acc += b
#         day += 1

# print(day)

# 通过50%的样例
# 查看用例规模：a,b,n <= 10**18
# 下载来用例一看，最恶心的一个用例是：1 1 1000000000000000000
# 老6啊

# 那转变一下思路，换时间怎么样呢？
# 再看一下题目，a,b确定后每周的工作量是确定的，那样直接用n对工作量取模，剩下的再模拟求解即可


a,b,n = map(int, input().split())
acc = 0
day = 0
i = 0
week = [1,2,3,4,5,6,7]

weekload = a*5+b*2
Week = n // weekload
n = n - weekload*Week

while acc < n:
    i = (i+1) % 7
    if week[i] <= 5:
        acc += a
        day += 1
    elif week[i] > 5:
        acc += b
        day += 1

print(Week*7+day)