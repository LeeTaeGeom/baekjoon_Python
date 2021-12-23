def re(a,b):
    if b==0:
        return 0
    if a==0:
        return b
    else:
        return re(a,b-1)+re(a-1,b)
        
 

n=int(input())

for i in range(n):
    a=int(input())
    b=int(input())
    
    r=re(a,b)
    print(r)
