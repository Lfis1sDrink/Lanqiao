MOD = 10**9 + 7

# no number 0, 9998 bits

# every bit can be distrubuted by 1-8 (8 digitls)

ans1 = 9
for i in range(10000):
  ans1 = (ans1 * 9)

ans2 = 7
for i in range(10000):
  ans2 = (ans2 * 7)

ans = (ans1 - ans2) % MOD

print(ans)