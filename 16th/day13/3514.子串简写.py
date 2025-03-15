k = int(input())
s,c1,c2 = map(str, input().split())
n = len(s)
ans = 0
# 计算S中有多少个c1开头c2结尾的子串可以采用k8s这样的简写

# 思路1：先找a的位置，找到a的位置后再找从a+3开始有多少个b，就有多少个子串
# for i in range(n):
#   if s[i] == c1:
#     for j in range(i+k-1,n):
#       if s[j] == c2:
#         ans += 1
# print(ans)
# 通过了40%的测试用例，其它全部TLE，比如说有个例子是k=10000，s是ab重复了20000次组成的字符串
# 思路2，关键是要能快速读出某个字符从指定区间内出现了多少次，
# 新建一个列表用来存储目前所有字符出现的次数可行吗？
# 似乎也不行，列表虽然保存了所有的次数，但是还得想怎么才能找到字符最后出现的位置
# 那把某个区间内的字符串切分出来扔到一个字典里可以吗？这样可以快速得出某个字符出现的次数
# 但是需要频繁创建不同子字符串出现的字典
# 那么还是使用次数列表来快速求解吧
# 比如对于s = ababababaaababbba
# 可以创建l = 11223344567586789这样的列表，就可以快速得出某个区间内这个字符出现的次数了
# 那么开始吧

char_count = {}  # 用于存储每个字符的出现次数
l = []  # 用于存储结果

# 遍历字符串 s
for char in s:
    # 如果字符没有出现过，则初始化其出现次数为 0
    if char not in char_count:
        char_count[char] = 0
    # 增加字符的出现次数
    char_count[char] += 1
    # 将当前字符的出现次数添加到列表 l 中
    l.append(char_count[char])


# 边界条件错误，答案一直错误
# for i in range(n):
#   if s[i] == c1 and i+k <= n:
#     firstc2idx = i+k-1+s[i+k-1:].find(c2) 
#     lastc2idx = s.rfind(c2) 
#     ans = ans + (l[lastc2idx] - l[firstc2idx] + 1)
# print(ans)



# # 最后还是dpsk深度思考了，真牛
# k = int(input())
# s, c1, c2 = input().split()
# n = len(s)
# ans = 0

# # Preprocess the cumulative count for each character
# char_count = {}
# l = []
# for char in s:
#     if char not in char_count:
#         char_count[char] = 0
#     char_count[char] += 1
#     l.append(char_count[char])

# for i in range(n):
#     if s[i] == c1:
#         start = i + k - 1
#         if start >= n:
#             continue  # 子串长度不够k
#         # 查找start之后第一个c2的位置
#         first_pos = s[start:].find(c2)
#         if first_pos == -1:
#             continue
#         firstc2idx = start + first_pos
#         # 查找在start之后最后一个c2的位置
#         lastc2idx = s.rfind(c2, start)
#         if lastc2idx < start:
#             continue
#         # 确保这两个位置的字符确实是c2
#         if s[firstc2idx] != c2 or s[lastc2idx] != c2:
#             continue
#         # 计算数量
#         ans += l[lastc2idx] - l[firstc2idx] + 1

# print(ans)


# 尝试修正我的错误
for i in range(n):
  if s[i] == c1 and i+k <= n:
    firstc2idx = i+k-1+s[i+k-1:].find(c2) 
    lastc2idx = s.rfind(c2) 
    # 主要的问题就出在了没有加上下面这两行，因为没有考虑到c2可能会在c1之前找到的情况
    # 这会导致子串长度不满足却也计数的错误
    if lastc2idx < i+k-1:
        continue
    ans = ans + (l[lastc2idx] - l[firstc2idx] + 1)

print(ans)