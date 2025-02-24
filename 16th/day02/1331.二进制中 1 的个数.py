x= int(input())
ans =0
for i in range(32):
    if(x >> i)&1:
        ans += 1
print(ans)