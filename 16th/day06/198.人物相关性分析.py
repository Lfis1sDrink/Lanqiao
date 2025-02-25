# 2025-02-24时隔一个月继续开始学习，
# 中间一个月的时间在完成群聊小助手、过春节，现在继续学习

import re
import bisect

# k = int(input())
# s = input()


# lista = [m.start() for m in re.finditer(r"\bAlice\b",s)]
# listb = [m.start() for m in re.finditer(r"\bBob\b",s)]

# count = 0
# for i in range(len(lista)):
#     lo = bisect.bisect_left(listb, lista[i]-k-3)
#     up = bisect.bisect_right(listb, lista[i]+k+5)
#     count += up-lo
# print(count)



k = int(input())
s = input()

# lista是一个列表，保存了字符串中所有\bAlice\b的起始位置
# re.finditer(pattern, string)会返回一个匹配对象(match对象)的迭代器
# 每个匹配对象都包含更多的信息，如匹配的开始和结束位置等

# Return an iterator over all non-overlapping matches in the
# string. For each match, the iterator returns a Match object.
# Empty matches are included in the result.
lista = [m.start() for m in re.finditer(r"\bAlice\b",s)]
listb = [m.start() for m in re.finditer(r"\bBob\b",s)]


# 现在两个a,b两个列表中保存的就是所有\bAlice\b和\bBob\b的起始下标
# 下面开始计算\bAlice\b和\bBob\b的距离小于k的这样的匹配对的数量
count = 0

# AI们对bisect_left和bisect_right两个方法的解释非常学术，很不好理解，这里放上我的理解：
# 对于已存在的值，left和right方法的区别是一个向相同的值的最左边放一个向最有右边放；
# 对于不存在的值，两个方法都是保持有序的情况下直接放进去
for i in range(len(lista)):
    lo = bisect.bisect_left(listb, lista[i]-k-3)
    up = bisect.bisect_right(listb, lista[i]+k+5)
    count += up - lo

print(count)

 
