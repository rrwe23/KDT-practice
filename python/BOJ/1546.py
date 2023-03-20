# https://www.acmicpc.net/problem/1546

T = int(input()) # 우선 T만큼 과목을 받는다. 

score = list(map(int,input().split())) # 리스트로 과목의 점수를 받는다.

M = max(score) # 리스트에서 가장 큰 값을 지정한다.

f_score = 0 # 가짜 점수..를 0이라고 할 때


for j in score:  # 반복문을 통해 리스트에 있는 점수를 주어진 식에 넣고 이를 bad 라고 선언한다.
    bad = j/M*100
    f_score += bad          # bad를 하나하나씩 가짜 점수에 집어 넣는다. 

print((f_score) / T)    # 구해진 점수의 평균을 출력한다.




