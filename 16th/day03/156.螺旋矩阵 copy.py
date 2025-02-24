import os
import sys

# 请在此输入您的代码
list1 = list(map(int, input().split()))
list2 = []
n = list1[0]
N = n
Y = list1[1]
X = list1[2]
count = 0
is_even = False
num = 0
# 判断有几圈，以及圈数是偶数还是奇数
if n % 2 == 1:
    is_even = True
    count = 1 + int(n / 2)
else:
    is_even = False
    count = int(n / 2)
for i in range(count):
    if (X == i + 1 or Y == i + 1) or (X == N - i or Y == N - i):# 判断坐标在第几圈
        list2.append([i + 1, i + 1])
        if i == count - 1:# 判断在最后一圈
            if is_even:# 判断为奇数圈
                for j in range(n - 1):
                    x = list2[-1][0] + 1
                    y = list2[-1][1]
                    list2.append([x, y])
                print(list2.index([X, Y]) + 1 + num)
            else :# 判断为偶数圈
                for j in range(n - 1):
                    x = list2[-1][0] + 1
                    y = list2[-1][1]
                    list2.append([x, y])
                for j in range(n - 1):
                    x = list2[-1][0]
                    y = list2[-1][1] + 1
                    list2.append([x, y])
                for j in range(n - 1):
                    x = list2[-1][0] - 1
                    y = list2[-1][1]
                    list2.append([x, y])
                print(list2.index([X, Y]) + 1 + num)
        else:# 判断不在最后一圈
            for j in range(n - 1):
                x = list2[-1][0] + 1
                y = list2[-1][1]
                list2.append([x, y])
            for j in range(n - 1):
                x = list2[-1][0]
                y = list2[-1][1] + 1
                list2.append([x, y])
            for j in range(n - 1):
                x = list2[-1][0] - 1
                y = list2[-1][1]
                list2.append([x, y])
            for j in range(n - 1):
                x = list2[-1][0]
                y = list2[-1][1] - 1
            print(list2.index([X, Y]) + 1 + num)
            break
    num += 4 * n - 4
    n -= 2