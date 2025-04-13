n =int(input())

# def GoodNum(reversed_n):
#   i = 0
#   flag = True
#   while i < len(reversed_n):
#     if int(reversed_n[i]) % 2 == 0:
#       flag = False
#     i += 2
#   i = 1
#   while i < len(reversed_n):
#     if int(reversed_n[i]) % 2 != 0:
#       flag = False
#     i += 2
#   return flag

# ans = 0
# for i in range(1,n+1):
#     n2str = str(i)
#     if GoodNum(list(reversed(n2str))):
#         ans += 1

# print(ans)

# 通过90%的样例，剩一个超时了

odd = ['1','3','5','7','9']
even = ['0','2','4','6','8']

# 1000_0000
# _bcd_efgh
#  oeo_eoeo
# o代表odd奇数 e代表even偶数

res = set()
for b in odd:
   for c in even:
      for d in odd:
         for e in even:
            for f in odd:
               for g in even:
                  for h in odd:
                     res.add(int(h))
                     res.add(int(g+h))
                     res.add(int(f+g+h))
                     res.add(int(e+f+g+h))
                     res.add(int(d+e+f+g+h))
                     res.add(int(c+d+e+f+g+h))
                     res.add(int(b+c+d+e+f+g+h))


res = list(res)

res.sort()

i = 0
cnt = 0
while res[i] <= n:
   # print(res[i])
   cnt += 1
   i += 1

print(cnt)


2024
1
3
5
7
9
21
23
25
27
29
41
43
45
47
49
61
63
65
67
69
81
83
85
87
89
121
123
125
127
129
141
143
145
147
149
161
163
165
167
169
181
183
185
187
189
321
323
325
327
329
341
343
345
347
349
361
363
365
367
369
381
383
385
387
389
521
523
525
527
529
541
543
545
547
549
561
563
565
567
569
581
583
585
587
589
721
723
725
727
729
741
743
745
747
749
761
763
765
767
769
781
783
785
787
789
921
923
925
927
929
941
943
945
947
949
961
963
965
967
969
981
983
985
987
989