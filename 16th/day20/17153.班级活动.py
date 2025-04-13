n = int(input())
a = list(map(int, input().split()))


flag = [[0]*10**5,[0]*10**5]

morethan2s = []

for i in range(n):
  if flag[0][a[i]] == 0:
    flag[0][a[i]] = 1
  elif flag[1][a[i]] == 0:
    flag[1][a[i]] = 1
  else:
    morethan2s.append(a[i])

print(morethan2s)
ans = 0
if len(morethan2s) < n-len(morethan2s):
  ans += len(morethan2s)

cunt = 0
for i in range(n):
  if flag[0][a[i]] == 1 and flag[1][a[i]] == 1:
    continue
  cunt += 1
ans = ans + cunt
print(ans)