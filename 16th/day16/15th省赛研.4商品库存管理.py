# # def howManyZero(aList):
# #   count = 0
# #   for _ in range(len(aList)):
# #     if aList[_] == 0:
# #       count += 1
# #   return count




# n,m = map(int, input().split())

# ml = []
# mr = []


# for _ in range(m):
#   l,r = map(int, input().split())
#   ml.append(l)
#   mr.append(r)

# # def do(alist, group):
# #   begin = ml[group]-1
# #   end = mr[group]-1
# #   for i in range(begin,end+1,1):
# #     # if i < begin:
# #     #   continue
# #     # if i > end:
# #     #   break
# #     # if begin <= i <= end:
# #       alist[i] += 1


# for i in range(m):
#   goodsList = [0]*n
#   for j in range(m):
#     if i == j:
#       continue
#     # 执行操作
#     begin = ml[j]-1
#     end = mr[j]-1
#     for x in range(begin,end+1,1):
#       goodsList[x] += 1
#   print(str(goodsList).count('0'))
    


# # 4868 1488
# # 40 58
# # 2454 2470
# # 1222 1230
# # 2580 2595
# # 3453 3473


n,m = map(int, input().split())

ml = []
mr = []

for _ in range(m):
  l,r = map(int, input().split())
  ml.append(l)
  mr.append(r)

for i in range(m):
  goodsList = [0]*n
  for j in range(m):
    if i == j:
      continue
    # 执行操作
    begin = ml[j]-1
    end = mr[j]-1
    for x in range(begin,end+1,1):
      goodsList[x] += 1
  ans = 0
  for _ in range(n):
    if goodsList[_] == 0:
      ans += 1
  print(ans)