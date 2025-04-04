MOD = 10**9 + 7

# no number 0, 9998 bits

# every bit can be distrubuted by 1-8 (8 digitls)

ans1 = 9**1000

ans2 = 7**1000

ans3 = 8**1000

ans = (ans1 - 2*ans3 + ans2) % MOD

print(ans)