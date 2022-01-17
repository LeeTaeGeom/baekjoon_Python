import sys
import math
b=10000
l=[0]*(b+1)
l[0]=1
l[1]=1
for i in range(2,int(math.sqrt(b))+1):
    for j in range(i*i,b+1,i):
        l[j]=1
r=[]
for k in range(2,b+1):
    if l[k]==0:
        r.append(k)    
        
a=int(sys.stdin.readline())
for i in range(a):
    
    j=int(sys.stdin.readline())
    gp=0
    while(1):
       
        
        k1=j//2-gp
        k2=j//2+gp
        if k1 in r:
            if k2 in r:
                print(k1,k2)   
                break         
        gp+=1
            
