"""
对于给定的自然数 `n`，按照题意可以在前面依次拼上不超过 `n` 一半的数，形成这样一个数列：  
`1|n, 2|n, 3|n, ..., n//2|n`
对于这个数列里的每个数，继续按照上述规则进行处理。
对于添加过的每个数字，又能添加几个数字，这和 `n` 的问题是一样的，因此只要考虑 `n` 能添加几次就好了。
也就是说，对每个子问题的处理方法都是和最开始的问题处理方法一样。
那么就开始递归。

"""

def addnum(n):
  if n == 1:
    return 1
  ans = 1
  for i in range(1,n // 2 +1):
    ans += addnum(i)
  return ans

i = int(input())
print(addnum(i))
