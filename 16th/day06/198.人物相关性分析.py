# 2025-02-24时隔一个月继续开始学习，
# 中间一个月的时间在完成群聊小助手、过春节，现在继续学习

import re
import bisect

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
