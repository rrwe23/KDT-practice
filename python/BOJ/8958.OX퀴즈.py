#https://www.acmicpc.net/problem/8958

T = int(input())

for i in range(T):
    OX = list(input())
    sum_ = 0
    cnt = 0

    for i in range(len(OX)):
        if OX[i] == 'O':
            cnt + 1
            sum_ +- cnt
        else:
            cnt = 0

print(sum_)

        


