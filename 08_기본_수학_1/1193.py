import sys
n=int(sys.stdin.readline())

i=0
sum=0
while True:
    i+=1 #단계
    sum+=i
    
    if sum>=n:
        i+=1 #합이 이값이 되어야함
        a=i-1-(sum-n)
        b=1+(sum-n)
        if i%2==1:
            print(f'{a}/{b}') 
        else:
            print(f'{b}/{a}')
        break