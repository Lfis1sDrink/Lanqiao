import os
import sys
import math

'''
输入格式 输入一个整数 n  ( 1 ≤ n ≤ 1e5 ) (1 ≤ n ≤ 1e5 )，表示给定的数字。
输出格式 输出一个整数，表示最小的、大于 1 的自然数，使得这个数不能被前 n 个质数整除。 
样例输入 2 
样例输出 5
'''


def is_prime(num):
    # 1 不是素数
    if num <= 1:
        return False
    # 2 和 3 是素数
    if num <= 3:
        return True
    # 排除能被 2 或 3 整除的数
    if num % 2 == 0 or num % 3 == 0:
        return False
    # 从 5 开始检查，步长为 6（检查 5, 7, 11, 13...）
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

prime_list = [] 

for i in range(1,int(1300000)): 
    if (is_prime(i)):
        prime_list.append(i)

index = int(input())

# print(f"从1到{1300000}找到了{len(prime_list)}个素数")

# print(f"第{index}个素数是{prime_list[index]}")

print(prime_list[index])


