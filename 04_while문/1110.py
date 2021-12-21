a=int(input())
ans=a
t=0
while(True):

    s=a//10+a%10
    a = (a % 10) * 10 + s % 10

    t += 1
    if ans==a:
        break
    else:
        continue
print(t)