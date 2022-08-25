#1부터 n까지의 합을 구하여 출력하는 코드를 
#1) while 문 2) for 문으로 각각 작성하시오.

#sum() 함수 사용 금지

n = int(input())        

count = 0
result = 0

# while result < n * (n+1) // 2:   # while
#     result += count
#     count += 1



for i in range(1, n *(n+1)//2 + 1):     # for

    result += 1

print(result)




