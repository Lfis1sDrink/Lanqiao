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

# print(l)
# k -= 1
for i in range(n):
  if s[i] == c1 and i+k <= n:
    firstc2idx = i+k-1+s[i+k-1:].find(c2) #i+k个位置后c2第一次出现的位置
    lastc2idx = s.rfind(c2) #找到最后一个c2出现的位置
    # print(f"从{firstc2idx}到{lastc2idx}的位置")
    ans = ans + (l[lastc2idx] - l[firstc2idx] + 1)
    # print(f"c2共有{l[lastc2idx]}-{l[firstc2idx]} +1 = {l[lastc2idx] - l[firstc2idx] + 1}次")
print(ans)
