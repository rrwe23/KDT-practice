#https://www.acmicpc.net/problem/2920

lyric = list(map(int,input().split()))

if lyric == sorted(lyric):
    print("ascending")
elif lyric == sorted(lyric,reverse = True):
    print("descending")
else:
    print("mixed")



