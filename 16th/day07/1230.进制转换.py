"""
这题纯背诵题，任意进制的转换十分简单，只要
以`10进制`为纽带，会写这两个函数就好:
```
K_to_ten(K, number_base_K)
##K_to_ten任意进制转10进制，可以用int(S,N)代替，S为字符串数，N为原始进制
Ten_to_K(number_base_ten, K)
```
"""

def convert_to_base(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"  # 支持16进制数
    result = ""
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
        
    return result

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  S = input()
  #N进制的S转为M进制的数输出
  print(convert_to_base(int(S,N), M))

