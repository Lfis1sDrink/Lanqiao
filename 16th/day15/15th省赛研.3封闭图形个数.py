"""
print(a[20:30])
# 34105, 13535, 56948, 20936, 41827, 76639, 21576, 
# 20856, 9821, 56091, 88463, 81315, 70996, 84471, 
# 29622,33740, 43523, 96920, 22167, 4355, 25122, 
# 26760, 20944, 21873,  93092, 81599, 45792]

# 234105, 13535, 556948, 320936, 341827, 376639, 121576, 
# 320856, 39821, 356091, 688463, 281315, 470996, 484471, 


关键是前面拼接了数字以后排好序再怎么恢复原来的数字呢？
不行
拼好了以后就没机会还原了？
保存下标可以不呢？

引入字典呢？

想想怎么搞

分组排序呢？

前面拼1的一组
拼2的一组
拼3的一组
扔进去排序
然后再按1,2,3的顺序把不同组拼起来
可行吗？

试试
# 18 29 6 34105, 13535, 56948, 20936, 41827, 76639, 21576, 
# 补0 13535
# 补1 29 6 21576
# 补2 18 34105 
# 补3 20936 41827 76639
# 补4 
# 补5 56948
然后拼接补0补1补2补3补4补5 就是结果！可行
"""
import itertools

n = int(input())

a = list(map(int, input().split()))

baseL = [[] for _ in range(19)]

for i in range(n):
  #对每个数字判断它的封闭图形个数，之后分别放到对应的列表里排序
  a_str = str(a[i])
  a_count = a_str.count('0') + a_str.count('4') + a_str.count('6') + a_str.count('9') + (a_str.count('8'))*2
  baseL[a_count].append(a[i])


baseL = [sorted(baseL[i]) for i in range(19)]
res = list(itertools.chain(*baseL))

# for i in range(18):
#   res.append(baseL[i])

for i in range(len(res)):
  print(res[i],end=" ")

# Debug：
# 18
# 65 103 156 265 292 345 453 1134 1247 2052 2055 2226 2229 2392 23 18 29 6
# [6, 29, 65, 103, 156, 265, 292, 345, 453, 1134, 1247, 2052, 2055, 2226, 2229, 2392, 18, 23]
