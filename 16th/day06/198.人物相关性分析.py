# 2025-02-24时隔一个月继续开始学习，
# 中间一个月的时间在完成群聊小助手、过春节，现在继续学习
# 2025-03-06 事实上，我并没有继续学习，而是不得不在做什么英语PPT蒸发冷却PPT什么的，一些其他的事情，现在继续学习

import re
#re直译是regular expression的缩写，是正则表达式的意思
#re模块是python内置的一个用于处理正则表达式的模块
#re.finditer(pattern, string, flags=0) 返回一个迭代器，迭代器中的元素是匹配到的字符串的位置
import bisect
#bisect直译是二分法的意思，是python内置的一个模块，用于处理已排序的序列
#bisect.bisect_left(a, x, lo=0, hi=len(a)) 返回在有序序列a中插入x的位置，如果x已经存在，则插入在左侧
#bisect.bisect_right(a, x, lo=0, hi=len(a)) 返回在有序序列a中插入x的位置，如果x已经存在，则插入在右侧
#lo是缩写low，hi是缩写high，lo和hi是可选参数，用于指定搜索的范围，默认是整个序列

k = int(input())
s = input()

lista = [m.start() for m in re.finditer(r"\bAlice\b",s)]
listb = [m.start() for m in re.finditer(r"\bBob\b",s)]

count = 0
for i in range(len(lista)):
    lo = bisect.bisect_left(listb, lista[i]-k-3)
    up = bisect.bisect_right(listb, lista[i]+k+5)
    count += up-lo
print(count)
