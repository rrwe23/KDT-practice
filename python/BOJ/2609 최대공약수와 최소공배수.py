# https://www.acmicpc.net/problem/2609

# import math

#print(math.gcd(a,b)) 최대공약수 구하기
#print(math.lcm(a,b)) 최소공배수 구하기

a,b = map(int,input().split())

n,m = max(a,b),min(a,b)

while m >0:
    n,m = m, n % m

print(n)
print((a*b)//n)
