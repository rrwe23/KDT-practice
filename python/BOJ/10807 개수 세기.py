# https://www.acmicpc.net/problem/10807

_list = []
cnt = 0
N = int(input())


num = list(map(int,input().split()))


my_num = int(input())

for i in num:
    if i == my_num:
        cnt += 1

print(cnt)