import sys

S=sys.stdin.readline().strip()

for i in range(ord('a'),ord('z')+1):
    
    if chr(i) in S:
        print(S.index(chr(i)),end=' ')
    else:
        print(-1,end=' ')