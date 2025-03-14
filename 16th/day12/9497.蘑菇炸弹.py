"""
## 问题描述

题莫作为《XX联盟》最受欢迎的人气英雄，用其独有的技能机制荣获光荣头衔——团战可以输，题莫必须死。

具体地说，题莫种下了 `n` 个蘑菇炸弹，其中第 `i` (`i ∈ [1, n]`) 个蘑菇的爆炸能力为 `a_i`。为此，瓦罗兰大陆著名的拆弹专家及格撕，受命来拆除这 `n` 个蘑菇炸弹，但他时间有限，只愿拆除那些高爆蘑菇炸弹。

若一个蘑菇炸弹满足以下条件则被称为高爆蘑菇炸弹：

- `2 ≤ i ≤ n − 1`
- `a_i ≥ a_(i-1) + a_(i+1)`

请你帮及格撕求出高爆蘑菇炸弹的数量。

## 输入格式

第一行输入一个整数 `n`，表示题莫种下的蘑菇炸弹的数量。

第二行输入 `n` 个整数 `a_1, a_2, a_3, ⋯, a_n`，表示每个蘑菇炸弹的爆炸能力。

## 输出格式

输出一个数字，表示高爆蘑菇炸弹的数量。

"""
n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(1,n-1):
  if a[i] >= (a[i-1] + a[i+1]):
    ans += 1


print(ans)