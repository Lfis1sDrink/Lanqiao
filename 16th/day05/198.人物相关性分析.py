import re

k = int(input())
str = input()


#先把Alice的所有位置下标找出来
index = []
begin = 0



#从每一个开始向后找K个位置，用正则表达式找(,. ?)Bob(,. ?)
