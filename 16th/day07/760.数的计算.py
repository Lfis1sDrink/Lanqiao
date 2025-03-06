def addnum(n):
  if n == 1:
    return
  print(n)
  for i in range(1,int(n/2)):
    addnum(int(str(i)+str(n)))
    count += 1
  



i = int(input())
count = 0
addnum(i)
print(count)
