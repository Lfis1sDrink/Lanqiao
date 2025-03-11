# 请在此输入您的代码

# *OO*O*O**O*
# ***ooo*****

# **********
# oo********
# oo**oo****
# o*o*oo****
# o*oo*o****
# o****o****
# o****o****

# *OO*O*O**O*
# ****O*O**O*
# ***o**O**O*
# ***oooO**O*
# ***ooo*o*O*
# ***ooo**oO*
# ***ooo*****
# ***ooo*****

# *O**O*O*OOO*OO**OOO****O*O*O*OO
# **O*O*O*OOO*OO**OOO****O*O*O*OO
# ***OO*O*OOO*OO**OOO****O*O*O*OO
# ***O*OO*OOO*OO**OOO****O*O*O*OO
# ***O****OOO*OO**OOO****O*O*O*OO
# ......
# ***O******O*OOOO*O*O*O*O*O***O*

# 思路：读入字符串，o和*分别当作-1，1处理，左边指针指向待处理字符串，
# 向右开始找第一个不相同的元素，(找到后将此位置和下一个位置的元素取反，次数+1), 指针+1
# 继续此过程

# !!!!!.....
# **********
# OO********
# O*O*******
# O**O******
# O***O*****
# O****O****
# o****o****


# **O*
# **O*
origin = input()
todo = input()

origin = [-1 if c == '*' else 1 for c in origin]
todo = [-1 if c == '*' else 1 for c in todo]
ans = 0
l,r = map(int, (0,0))

while l < len(origin):
  if origin == todo:
    break
  if origin[l] != todo[l]:
    origin[l] = -origin[l]
    origin[l+1] = -origin[l+1]
    ans += 1
  l+=1

print(ans)