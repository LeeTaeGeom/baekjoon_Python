import sys

l=[ int(sys.stdin.readline().rstrip()) for i in range(9)]
maxl=max(l)
il=l.index(maxl)+1
print(maxl)
print(il)