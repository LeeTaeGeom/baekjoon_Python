import sys
s=sys.stdin.readline().strip()
l=['c=','c-','dz=','d-','lj','nj','s=','z=']
c=0
for i in l:
    if s.count(i):
        c-=s.count(i)*len(i)-s.count(i)
if s.count('dz='):
    c+=(2*s.count('dz=')-s.count('dz='))
print(len(s)+c)
