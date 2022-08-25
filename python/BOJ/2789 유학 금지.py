#https://www.acmicpc.net/problem/2789

a = input().upper()

for i in 'CAMBRIDGE':
    a = a.replace(i,'')

print(a)
