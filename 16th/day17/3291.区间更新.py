#差分数组

while True:
  try:
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    diff = [0] * (n+1)
    diff[0] = a[0]
    for i in range(1,n):
      diff[i] = a[i] - a[i-1]
    for i in range(m):
      x,y,z = map(int, input().split())
      diff[x-1] += z
      diff[y] -= z
    # a[0] = diff[0]
    for i in range(1,n):
      diff[i] = diff[i] + diff[i-1]
    a = diff[:n]
    print(' '.join(map(str, a)))
  except Exception as e:
    print(e)
    break





