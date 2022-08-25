# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))
for i in range(10):
    print(result.count(str(i)))





