import os
import sys

# 请在此输入您的代码

s = input()
sum1,sum2 = 0,0

for char in s:
  if char in "aeiou":
    sum1+=1
  else:
    sum2+=1

print(sum1)
print(sum2)