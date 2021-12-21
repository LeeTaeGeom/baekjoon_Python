import sys

def find(n):
    s=0
    for i in range(1,n+1):
        if i <100:
            s+=1
        else:
            c=i
            g=10 #-9~9가아닌 아무수
            
            while(c>0):
                o=c%10
                oo=c%100//10
                
                if(g==10):
                    g=oo-o
                    c=c//10
                  
                else:
                    if c<10:
                        # print(i)
                        s+=1
                    if g==oo-o:
                        c=c//10
                        continue
                    else:
                        break
           
            
                
                
    return s

n=int(sys.stdin.readline())
s=0
print(find(n))