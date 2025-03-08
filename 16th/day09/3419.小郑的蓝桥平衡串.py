"""
## 问题描述
平衡串指的是一个字符串，其中包含两种不同字符，并且这两种字符的数量相等。
例如：

- `ababab` 和 `aababb` 都是平衡串，因为每种字符各有三个，而 
- `abaab` 和 `aaaab` 都不是平衡串，因为它们的字符数量不相等。

平衡串在密码学和计算机科学中具有重要应用，比如可以用于构造哈希函数或者解决一些数学问题。
小郑拿到一个只包含 `L` 和 `Q` 的字符串，他的任务就是找到最长平衡串，且满足平衡串的要求，即保证子串中 `L` 和 `Q` 的数量相等。
### 输入格式
输入一行字符串，保证字符串中只包含字符 `L` 和 `Q`。

### 输出格式
输出一个整数，为输入字符串中最长平衡串的长度。

### 样例输入
```
LQLL
```

### 样例输出
```
2
```

将L、Q转换成数字, 例如L为+1、Q为-1, 问题就变成求区间和为0的最长区间
枚举所有的区间即可.
"""
from itertools import accumulate

def rangesum(isapresum,l,r):
    if l == 0:
        return isapresum[r]
    else:
        return isapresum[r] - isapresum[l-1]


string = input()
string2numlist = [-1 if char == 'L' else 1 for char in string]


presum = list(accumulate(string2numlist))
value = 0

for i in range(0, len(string2numlist)):
    for j in range(i, len(string2numlist)):
        if rangesum(presum,i,j) == 0:
            value = max(value,j-i+1)
print(value)

# print(string2numlist)
# print(presum) 