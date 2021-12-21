from collections import Counter
import sys
l=[ int(sys.stdin.readline().strip())%42 for i in range(10) ]
print(len(Counter(l)))