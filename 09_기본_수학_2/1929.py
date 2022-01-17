import sys
import math
a,b=map(int,sys.stdin.readline().split())

l=[0]*(b+1)
l[0]=1
l[1]=1
for i in range(2,int(math.sqrt(b))+1):
    for j in range(i*i,b+1,i):
        l[j]=1
r=[]
for i in range(a,b+1):
    if l[i]==0:
        print(i)