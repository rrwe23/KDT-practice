# https://www.acmicpc.net/problem/23825

cnt = 0

S,A = map(int,input().split())

S_block = S // 2
A_block = A // 2

print(min(S_block,A_block))
