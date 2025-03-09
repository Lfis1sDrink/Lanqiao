N,K = map(int, input().split())
S = input()
 
newstring = S*K
# print(newstring)

times = 0
for i in range(len(newstring)):
    if newstring[i] == 'a':
        times += newstring[i:N].count('b')

print(times)