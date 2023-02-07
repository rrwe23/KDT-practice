#https://www.acmicpc.net/problem/5597

s = [i for i in range(1,31)]

for _ in range(28):
    num = int(input())
    s.remove(num)

print(min(s))
print(max(s))