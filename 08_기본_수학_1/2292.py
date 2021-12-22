import sys
n=int(sys.stdin.readline())

c=1
s=1
while True:
    if s<n:
        c+=1
        s+=6*(c-1)
    else:
        break
print(c)