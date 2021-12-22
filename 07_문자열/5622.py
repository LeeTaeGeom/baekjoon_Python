import sys
s=sys.stdin.readline().strip()
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="22233344455566677778889999"

mt=str.maketrans(a,b)
s=s.translate(mt)

sum=0
for i in s:
    sum+=int(i)+1
    
print(sum)