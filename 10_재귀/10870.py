import sys
def fibo(a,b,now,fin):
    if fin==0:
        return 0
    if now==fin:
        return b
    return fibo(b,a+b,now+1,fin)
n=int(sys.stdin.readline())
print(fibo(0,1,1,n))