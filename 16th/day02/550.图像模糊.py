def input_list():
  return list(map(int, input().split()))

n,m = input_list()
photo = []
photo_edit = [[0]*m for _ in range(n)]

for i in range(n):
  photo.append(input_list())

# (-1,-1)(-1, 0)(-1, 1)
# ( 0,-1)( 0, 0)( 0, 1)
# ( 1,-1)( 1, 0)( 1, 1)


delta = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

for i in range(n):
  for j in range(m):
    sum,cont = 0,0
    for k in range(9):
      x,y = i+delta[k][0], j+delta[k][1]
      if (0<= x <n) and (0<= y <m):
        sum += photo[x][y]
        cont += 1
    photo_edit[i][j] = int(sum/cont)
    print(photo_edit[i][j],end=' ')
  print()

  #错误1:开始直接对photo数组操作，导致结果会越来越大，实际按题意原数组应该是只读的
  #错误2:int(sum/cont)写成了int((photo[i][j]+sum)/cont),导致原数组是0的位置结果对，不是0的位置结果偏大