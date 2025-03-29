# 找不超过当前数字的最大的质数
# 1 <= ni <= 10**5

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primeList = [0]*(10**5)

for i in range(10**5):
  if not is_prime(i):
    continue
  primeList[i] = 1


#开始对局
def trunToLan(x):
  if x == 1:
    print(1)
    return
  p = x
  for i in range(x,1,-1):
    if primeList[i] == 1:
      p = i
      break
  if x-p == 0:
    print(0)
    return
  return trunToJohn(x-p)


def trunToJohn(x):
  if x == 1:
    print(0)
    return
  p = x
  for i in range(x,1,-1):
    if primeList[i] == 1:
      p = i
      break
  if x-p == 0:
    print(1)
    return
  return trunToLan(x-p)


# trunToLan(96)

t = int(input())
for _ in range(t):
  trunToLan(int(input()))
  # print(input())





"""
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 


59
83
79
37
21
33
69
96
56
98
43
8
40
89
34
31
58
12
89
62
36
36
"""