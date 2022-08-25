#주어진 숫자의 평균을 구하는 코드를 작성하시오.
#sum(), len()  함수 사용 금지

numbers = [3,10,20]

total = 0
count = 0

for i in numbers:
    total += i
    count += 1
print(int(total/count))




