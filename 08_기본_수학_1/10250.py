import sys
c=int(sys.stdin.readline())

for i in range(c):
    h,w,n=map(int,sys.stdin.readline().split())
    
    if n%h==0:
        print(h*100+(n//h))
    else:
        print(100*(n%h)+(n//h+1))
        
