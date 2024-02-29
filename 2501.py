N, M = map(int, input().split())
divide = []

for i in range(1, N + 1):
    if N % i == 0:
        divide.append(i)

if M <= len(divide):  # M이 divide 리스트의 길이를 초과하지 않는 경우
    print(divide[M - 1])
else:
    print(0)  # M이 divide 리스트의 길이를 초과하는 경우
