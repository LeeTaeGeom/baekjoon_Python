import sys
from collections import Counter

S=sys.stdin.readline().strip()
s=S.upper()
sc=Counter(s)

mc=-1
c=0
for i,j in sc.most_common():
    if mc==j:
        c+=1
    if mc<j:
        mc=j
if c==0:
    print(sc.most_common()[0][0])
else:
    print('?')
    