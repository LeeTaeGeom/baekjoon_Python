import sys
           
#a층 b호 , b는 14이하   
n=int(sys.stdin.readline())
l=[]
for i in range(n):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    l=[ i+1 for i in range(b) ]
    
    for i in range(a):
        for j in range(b):
            if j>0:
                l[j]=l[j-1]+l[j]
            
    print(l[b-1])