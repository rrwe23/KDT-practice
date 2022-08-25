#https://www.acmicpc.net/problem/10818

N = int(input())


my = list(map(int,input().split()))
my.sort()

print(my[0],my[-1])
