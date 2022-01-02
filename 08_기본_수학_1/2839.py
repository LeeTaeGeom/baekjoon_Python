import sys
n=int(sys.stdin.readline())
re=n
s=0
for i in range(n//5+1):
    for j in range(n//3+1):
        if 5*i+3*j==n:
            s=1
            if re>=i+j:
                re=i+j
if s==0:
    print(-1)
else:
    print(re)