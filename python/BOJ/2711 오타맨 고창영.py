#https://www.acmicpc.net/problem/2711

T = int(input())

for i in range(T):
    delete_,letter = input().split()
    delete_ = int(delete_)
    print(letter[:delete_-1], letter[delete_:],sep='')

