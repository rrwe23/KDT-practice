#https://www.acmicpc.net/problem/1065

N = int(input())
han = 0

for i in range(1,N+1):
    if i <= 100:
        han += 1
    else:
        my_list = list(map(int,str(i)))  #  [1,0,1]
        if my_list[0] -my_list[1] == my_list[1] - my_list[2]:
            han += 1

print(han)