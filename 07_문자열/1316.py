import sys
n=int(sys.stdin.readline())
r=0
for i in range(n):
    a=sys.stdin.readline().strip()
    length=ord('z')-ord('a')+1
    l=[0]*length
    s=0
    contin=''
    for j in a:
        if l[ord(j)-ord('a')] ==0:
            l[ord(j)-ord('a')]+=1
            s+=1
            contin=j
            continue
        elif contin == j:
            l[ord(j)-ord('a')]+=1
            s+=1
            contin=j
            continue
        elif contin != j:
            contin=j
            continue
        else:
            break
    if s==len(a):
        r+=1
print(r)