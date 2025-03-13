#公式化简，然后利用前缀和来快速求出区间和，从而求解
n = int(input())
s = list(map(int,input().split()))
ans = 0

def presum(needalist):
  prefix_sum = [0]*n

  for i in range(len(needalist)):
    if i == 0:
      prefix_sum[0] = needalist[0]
    prefix_sum[i] = prefix_sum[i-1] + needalist[i]
  
  return prefix_sum

prefix_sum = presum(s)


def rangesum(needalist,l,r):
  if l == 0:
    return prefix_sum[r]
  else:
    return prefix_sum[r] - prefix_sum[l-1]

for i in range(n):
  ans = ans + s[i]*rangesum(s,i+1,n-1)

print(ans)


"""
求和-lanqiao7790887134的代码
解题思路
原式=（和的平方-平方的和）*0.5
```python
n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
s=s*s
for i in arr:
  s-=i*i

print(s//2)
```

"""