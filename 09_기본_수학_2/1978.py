import sys
import math
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
s=0
for i in l:
    j=1
    while j<=int(math.sqrt(i)):
        if i==1:
            break
        if j!=1:        
            if i%j==0:
                break
        j+=1
    if j==int(math.sqrt(i))+1:
        s+=1
    
print(s)