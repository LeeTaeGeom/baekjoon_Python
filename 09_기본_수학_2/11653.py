import sys
import math
n= int(sys.stdin.readline())
fn=n
s=0
for i in range(2,n+1):
    
    while(n%i==0):
        print(i)
        n=n//i
        s+=1
