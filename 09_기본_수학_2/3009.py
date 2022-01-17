import sys
from collections import Counter

dx=[]
dy=[]
for i in range(3):
    x,y=map(int,sys.stdin.readline().split())
    dx.append(x)
    dy.append(y)

x=list(Counter(dx).items())
y=list(Counter(dy).items())
x.sort(key=lambda x: x[1])
y.sort(key=lambda x: x[1])
print(x[0][0],y[0][0])