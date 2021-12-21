def d(n,l):
    
    cn=n
    s=cn
    
    while(cn>0):
       s+=cn%10
       cn=cn//10
    
    
    if s>10000:
        return
    
    l[s-1]+=1

    d(s,l)
    

l=[0]*10000
for i in range(1,10001):
    d(i,l)

for i in range(1,10001):
    if l[i-1]==0:
        print(i)
