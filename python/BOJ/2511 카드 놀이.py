#https://www.acmicpc.net/problem/2511



A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_score = 0
B_score = 0
winner ='D'

for i in range(10):
    if A[i] > B[i]:
        A_score += 3
        winner = "A"
    elif A[i] < B[i]:
        B_score += 3
        winner = "B"
    elif A[i]==B[i]:
        A_score += 1
        B_score += 1
    
    
print(A_score,B_score,sep=' ')

if A_score > B_score:
    print("A")
elif A_score < B_score:
    print("B")
elif A_score == B_score:
    print(winner)





