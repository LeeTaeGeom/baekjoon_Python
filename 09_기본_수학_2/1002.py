import sys
n= int(sys.stdin.readline())
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    
    #같을때
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    #밖에서 접할때
    elif (x2-x1)**2+(y2-y1)**2==(r1+r2)**2:
        print(1)
    #안에서 접할때
    elif (x2-x1)**2+(y2-y1)**2 == (r2-r1)**2:
        print(1)
    # 두점 겹칠때
    elif (r2-r1)**2 < (x2-x1)**2+(y2-y1)**2 <(r1+r2)**2:
        print(2)
    else:
        print(0)