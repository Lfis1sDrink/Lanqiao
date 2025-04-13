# t = int(input())

# for i in range(t):
#   s = input()
#   reversed_s = s[::-1]
#   i = 0
#   while reversed_s[i] in ('l','q','b'):
#     i += 1
#   left_s = reversed_s[i:]
#   is_res = left_s == left_s[::-1]
#   print("Yes") if is_res else print("No")

# 通过40%，其余段错误，下载样例看看
# 样例不给下载，再找找bug，发现如果字符串只是lbq三个字母的话就会数组越界


t = int(input())

for i in range(t):
  s = input()
  reversed_s = s[::-1]
  i = 0
  while i < len(s) and reversed_s[i] in ('l','q','b'):
    i += 1
  left_s = reversed_s[i:]
  is_res = left_s == left_s[::-1]
  print("Yes") if is_res else print("No")

# 通过60%，剩下的答案错误，不是段错误了，
# 答案错误可以下载测试样例了，下载来看看
# 5
# dddpglqlbq
# fquysvnqbl
# qlbbllblbb
# sxkjjkxslq
# qqmwmqqqlb
# 运行：
# 5
# dddpglqlbq
# No
# fquysvnqbl
# No
# qlbbllblbb
# Yes
# sxkjjkxslq
# Yes
# qqmwmqqqlb
# No
# 正确答案：
# No
# No
# Yes
# Yes
# Yes
# qqmwmqqqlb应该是Yes的，但目前的算法会过多的匹配末尾的lbq，
# 导致剩下的字符串不是回文字符串了
# 解决办法：在末尾每匹配到一次lbq时候都检测一下剩余的是否是回文字符串

# t = int(input())

# for i in range(t):
#   s = input()
#   reversed_s = s[::-1]
#   i = 0
#   flag = 0
#   while i < len(s) and reversed_s[i] in ('l','q','b'):
#     left_s = reversed_s[i:]
#     is_res = left_s == left_s[::-1]
#     if is_res:
#       print("Yes")
#       flag = 1
#       break
#     i += 1
#   if flag == 0:
#     left_s = reversed_s[i:]
#     is_res = left_s == left_s[::-1]
#     print("Yes") if is_res else print("No")

# 通过70%，剩下的运行超时，再下载测试样例来看看
