import sys
n= int(sys.stdin.readline())
l= [ list(map(int,sys.stdin.readline().split())) for i in range(n)]
for i in l:
    e=sum(i[1:])/i[0]
    count=0
    for j in range(i[0]):
        if i[j+1]>e:
            count+=1
    ev=count/i[0]*100  
    print('{0:.3f}%'.format(ev))
        