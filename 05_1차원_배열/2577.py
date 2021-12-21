from collections import Counter
a=int(input())
b=int(input())
c=int(input())
m=a*b*c
m=str(m)
counter=Counter(m)
for i in range(10):
    print(counter[str(i)])
# list.count()로도 구할 수 있음