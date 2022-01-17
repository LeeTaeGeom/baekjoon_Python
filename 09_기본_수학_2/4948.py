import sys
import math

n=123456
l=[0]*(2*n+1)
l[0]=1
l[1]=1
for i in range(2,int(math.sqrt(2*n))+1):
    for j in range(i*i,2*n+1,i):
        l[j]=1
i=-1
while i != 0:
    i=int(sys.stdin.readline())
    if i==0:
        continue
    s=0
    for j in range(i+1,i*2+1):
        if l[j]==0:
            s+=1
    print(s)  
         