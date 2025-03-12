T = int(input())
for _ in range(T):
  s = input()
  s2l = "".join(set(s)) 
  if len(s2l) != 2:
    print("No")
    continue
  dic = {}
  for char in s:
    dic[char] = dic.get(char,0) + 1
  if (dic[s2l[0]] == 3 and dic[s2l[1]] == 1) or (dic[s2l[0]] == 1 and dic[s2l[1]] == 3):
    print("Yes")
  else:
    print("No")

