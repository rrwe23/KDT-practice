

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])       # [a0 a1 a2 a3 a4 a5.... an]

min = a[0]

for i in range(0,n):
    if a[i] < min:
        min = a[i]

print(min)



