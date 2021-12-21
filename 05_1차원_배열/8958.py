import sys
n=int(sys.stdin.readline().strip())

l=[sys.stdin.readline().strip() for i in range(n)]

for i in l:
    count = 0
    sum=0
    for j in i:
        if j=='O':
            count+=1
            sum+=count
        elif j=='X':
            count=0
    print(sum)
            