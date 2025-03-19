"""
# 自然数列的前缀和
# 找到问题了，没有考虑类似9=4+5这样的数字
def presum(needalist):
  a = needalist
  for i in range(1,len(a)):
    a[i] += a[i-1]
  return a

def rangesum(aPresumList,l,r):
  if l == 0:
    return aPresumList[r]
  elif l>r or l==r:
    return -1
  else:
    return aPresumList[r] - aPresumList[l-1]


n = int(input())
a = list(map(int, input().split()))

naturalNumberList = [i+1 for i in range(10**3)]
preNaturalNumberList = presum(naturalNumberList)


# flagList是映射，存储的是所有范围内的数字的满足状态，满足的下标位置的值为1，不满足的位置的值为0
flagList = [0]*(500501)


# 1到10**3的前缀和存储到flagList中
for i in range(10**3):
  flagList[preNaturalNumberList[i]] = 1
  for j in range(i,10**3):
    flagList[rangesum(preNaturalNumberList,i,j)] = 1

# 自然序列任意区间长的和存入flagList中


flagList[1] = 0

res = []

ans = 0
for i in range(n):
  if flagList[a[i]] == 1:
    ans += 1
    res.append(a[i])
# print(ans)
print(res)
# print(n-ans)


# 不太科学呀
# 找到可能出错的点了, 如果i>j也就是l>r的话，是不就会出错呢？也就是说我的区间和并没有考虑j>i的情况
# 比如说rangesum(preNaturalNumberList,14,0)会输出-104,这是程序会怎么处理呢？
# 按照Python列表的逻辑，-代表逆序，这就会导致我的所有的flagList都会被置为1
# 修改了这个错误后AC了，就是在rangsum中增加对l>r和l=r的判断
# 但是这样只通过了30%的用例，如果要通过100%的用例需要flagList = [0]*(20000100000), 这个数组是非常庞大的
# 该怎么做呢？10**16这个数字是非常大的,考虑bitmap试一下？
# 但是也不行，要使用bitmap的话需要开辟一个长度是10**16次方的数组，大小约为1PB...根本不可能
# 于是放弃

# 最后看解析了，进入和第2题也是一样的思路，先暴力求解，然后找规律，
# [1, 467, 1, 63, 1, 844, 1, 632, 1, 27, 1, 757, 1, 58,
#  0, 512, 1, 711, 1, 655, 1, 563, 1, 272, 1, 11, 1, 98,
#  1, 404, 1, 385, 1, 673, 0, 128, 0, 256, 1, 253]
# 观察发现只要是2的幂的数就没有诗意，那就好办了！
"""

# 接下来的问题就是怎么判断一个数是不是2的幂了
n = int(input())
a = list(map(int, input().split()))
ans = 0

powof2 = [pow(2,x) for x in range(54)]

for i in range(n):
  if a[i] in powof2:
    ans += 1

print(ans)


# 补充快速判断一个数是不是2的幂的方法：
# 1.
# def is_power_of_two(n):
#     return n > 0 and bin(n).count('1') == 1
# 2.
# if (a[i] & (a[i] - 1)) == 0:
#     ans += 1





