#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

from re import I


n = int(input())

cnt = 0
for i in range(1,n+1):
    if i % 2 ==0:
        cnt += i

print(cnt)

  
