#문자열 word가 주어질 때, 해당 문자열에서 a 가 
# 처음으로 등장하는 위치(index)를 출력해주세요.
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지

word = 'banana'

count = 0

# for i in word:
#     if i == 'b':
#         break
#     else:
#         count += 1
# if count ==len(word):
#     count = -1
# print(count)


# 문제 풀이

# for문을 다돌았다는 뜻은 한번도 break에 안걸렸다. 즉 a가 없었다.

for idx in range(len(word)):              #인덱스로 원하는 숫자 얻는 방법
    if word[idx]=='a':
        print(idx)
        break
    else:
        print(-1)
# print(idx, word[idx])   


# a가 있었냐 없었냐? ===(boolean)


 









