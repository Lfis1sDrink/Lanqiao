import os
import sys

# 请在此输入您的代码
n = int(input())

ans = 0

for i in range(1,n+1):
  if ('2' not in str(i) ):
    ans+=1
print(ans)