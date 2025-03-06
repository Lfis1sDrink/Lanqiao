# 2025-02-24时隔一个月继续开始学习，
# 中间一个月的时间在完成群聊小助手、过春节，现在继续学习
# 2025-03-06 事实上，我并没有继续学习，而是不得不在做什么英语PPT蒸发冷却PPT什么的，一些其他的事情，现在继续学习

import re
#re直译是regular expression的缩写，是正则表达式的意思
#re模块是python内置的一个用于处理正则表达式的模块
#re.finditer(pattern, string, flags=0) 返回一个迭代器，迭代器中的元素是匹配到的字符串的位置
import bisect

k = int(input())
s = input()


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

 
