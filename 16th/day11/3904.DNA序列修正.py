"""
思路: 

遍历所有元素如果互换两个位置后可以有两个元素的正确位置被找到则`ans+1`，

即`操作1`可进行的最大次数，

剩余的没处理过的元素全部使用`操作2`进行，即还有x个未处理元素就ans+x。

通过了`40%`的样例，下载测试样例后发现是`ATA/ATT`这个配对其实就是把`ATA`变成`TAA`可以一眼看出来只需要`1`步，但是代码输出的是`3`，然后发现最先应该考虑的是如果初始条件就有相同的应该先置`0`就是说跳过不考虑，这样操作后通过了`100%`的样例。
"""

n = int(input())

origin = list(input())
target = list(input())
for i in range(len(target)):
  if target[i] == 'A':
    target[i] = 'T'
  elif target[i] == 'T':
    target[i] = 'A'
  elif target[i] == 'C':
    target[i] = 'G'
  elif target[i] == 'G':
    target[i] = 'C'
l,r,ans = 0,n-1,0

for i in range(n):
  if origin[i] == target[i]:
    origin[i] = 0
    target[i] = 0


for i in range(n):
  for j in range(n):
    if j == i:
      continue
    if origin[i] == target[j] and origin[j] == target[i] and origin[i] != 0 and origin != target:
      ans += 1
      origin[i] = 0
      origin[j] = 0
      target[j] = 0
      target[i] = 0

for s in origin:
  if s != 0:
    ans += 1


print(ans)