#월이 입력될 때 계절 이름이 출력되도록 해보자.

a = int(input())

if a // 3 == 0:
    print("winter")
elif a // 3 == 1:
    print('spring')
elif a // 3 == 2:
    print('summer')
elif a // 3 == 3:
    print('fall')
else:
    print('winter')

