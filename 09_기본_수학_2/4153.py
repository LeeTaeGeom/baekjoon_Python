import sys
from collections import Counter
while(1):
    l=list(map(int,sys.stdin.readline().split()))
    if Counter(l)[0]==3:
        break
    l.sort()
    if l[0]*l[0]+l[1]*l[1]==l[2]*l[2]:
        print('right')
    else:
        print('wrong')