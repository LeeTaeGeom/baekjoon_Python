import sys
s=list(map(int,sys.stdin.readline().split()))
a=s[0]%10*100+s[0]//10%10*10+s[0]//100
b=s[1]%10*100+s[1]//10%10*10+s[1]//100
print(a if a>b else b)
