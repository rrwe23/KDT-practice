#문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
#len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

word = str(input())   # while 활용

i = 0
j = 0

# while (i < len(word)):
#     i += 1
# print(i)

          # for 활용
# for i in word:
#     j += 1
# print(j)

for i in range(len(word)):   # for index
    j += 1

print(j)



