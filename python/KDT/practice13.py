word = 'apple'              #방법1
result = ''
for char in word:
    result = char + result
print(result)

for i in range(len(word)):              #방법2
    print(word[len(word)-i-1],end ='')
   

#print(word[::-1])   방법3



for i in range(5):
    print(range(5))



# sep = 여러개를 동시에 출력할 때 사이에 구분값
# end = print 출력 이후 뒤에 뭐를 붙일지