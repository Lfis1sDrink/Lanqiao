import os
import sys

# 请在此输入您的代码
k=int(input())
def getprime(n):
    vis=[0]*(n+1)
    prime=[]
    for i in range(2,n+1):
        if vis[i]==0:
            prime.append(i)
        for now_prime in prime:
            if i*now_prime>n: break
            vis[i*now_prime]=1
            if i%now_prime==0: break
    return prime
#print(getprime(100))
ans=getprime(2*int(1e6))
#print(ans)
print(ans[k])