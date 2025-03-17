# 自然数列的前缀和

def presum(needalist):
  a = needalist
  for i in range(1,len(a)):
    a[i] += a[i-1]
  return a


n = int(input())
a = list(map(int, input().split()))

naturalNumberList = [i+1 for i in range(10**3)]
preNaturalNumberList = presum(naturalNumberList)

flagList = [0]*(500501)
for i in range(1000):
  flagList[preNaturalNumberList[i]] = 1
  
ans = 0
for i in range(n):
  if flagList[a[i]] == 1:
    ans += 1



print(n-ans)