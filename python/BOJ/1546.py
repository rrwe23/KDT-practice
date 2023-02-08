# https://www.acmicpc.net/problem/1546

T = int(input())
score = list(map(int,input().split()))

M = max(score)

f_score = 0


for j in score:
    bad = j/M*100
    f_score += bad

print((f_score) / T)




