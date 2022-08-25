#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지


# print(chr(ord(word[0])-32))           초기 구현 코드
# print(chr(ord(word[1])-32))
# print(chr(ord(word[2])-32))
# print(chr(ord(word[3])-32))
# print(chr(ord(word[4])-32))
# print(chr(ord(word[5])-32))


word = input()

result = ''

for i in word:
    temp = ord(i)
    temp -= 32
    result += chr(temp)

print(result)



# for char in word:
#     number = ord(char)
#     number = number - 32

#     print(chr(number))
