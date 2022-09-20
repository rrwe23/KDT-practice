# https://www.acmicpc.net/problem/1292

Dong = [0]
sum = 0

a, b = map(int,input().split())

for i in range(1,b+1):
    for j in range(i):
        Dong.append(i)

for i in range(a,b+1):
    sum += Dong[i]

print(sum)

