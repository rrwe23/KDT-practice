# https://www.acmicpc.net/problem/5622
list_ = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

grand = input()

second = 0

for i in range(len(grand)):
    for j in list_:
        if grand[i] in j:
            second += list_.index(j) + 3

    
print(second)


