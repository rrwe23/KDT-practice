## https://www.acmicpc.net/problem/1357


x, y = map(str, input().split())
s = str(int(x[::-1]) + int(y[::-1]))
print(int(s[::-1]))