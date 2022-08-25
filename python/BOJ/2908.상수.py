#https://www.acmicpc.net/problem/2908

A, B = map(int,input().split())

A = int(str(A)[::-1])
B = int(str(B)[::-1])

if A > B :
    print(A)
else:
    print(B)

    
