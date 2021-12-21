import sys
n=int(sys.stdin.readline().strip())
l=list(map(int,sys.stdin.readline().split()))

maxl=max(l)
l=[ i/maxl*100 for i in l]
# print(l)
print(sum(l)/n)
