#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
#max() 함수 사용 금지

numbers = [10000,950,20,850,1000,50,-60,50,100]

largest = numbers[0]
second = numbers[1]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif second < i < largest:
        second = i

print(second)

