import sys
a=int(sys.stdin.readline())
for i in range(a):
    n=sys.stdin.readline().split()
    
    for i in n[1]:
        print(i*int(n[0]),end='')
    print()