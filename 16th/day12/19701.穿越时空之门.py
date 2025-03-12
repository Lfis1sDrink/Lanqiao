"""
## 进制转换+遍历

考察进制转换，遍历1到2024输出二进制数位和 == 四进制数位和的次数。

主要难点在进制转换上，但只要记住会写10进制转2-16进制的函数就可以了

```python

#可以实现10进制转2-16进制的函数，返回一个字符串
def convert_base(num,baseWhat):
  digits = "0123456789ABCDEF"
  result = ""

  while num > 0:
    result = digits[num % baseWhat] + result
    num = num // baseWhat

  return result


def sum_byBase(i,baseWhat):
  sum = 0
  str2list = list(map(int,convert_base(i,baseWhat)))
  for digit in str2list:
    sum += digit
  return sum


ans = 0
for i in range(1,2025):
  if sum_byBase(i,2) == sum_byBase(i,4):
    ans += 1

print(ans)
```
"""

def convert_base(num,baseWhat):
  digits = "0123456789ABCDEF"
  result = ""

  while num > 0:
    result = digits[num % baseWhat] + result
    num = num // baseWhat

  return result



print(convert_base(16,16))