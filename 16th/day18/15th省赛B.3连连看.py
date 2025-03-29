n,m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split()))) 

count = 0
for a in range(n):
  for b in range(m):

    for c in range(n):
      for d in range(m):
        if arr[a][b] == arr[c][d] and a > c and b > d and a-c == b-d:
          count += 1

print(count)