import sys
input = sys.stdin.readline

n = int(input())
result = 0

# 1 ~ n까지 반복문 돌림
for i in range(1, n+1):
    # str(i) -> n의 각 자릿수를 문자열로 만듬
    # 이걸 map으로 쪼개면서 int 인자를 가진 List에 넣어줌.
    a = list(map(int, str(i)))
    # result에는 i값과 i의 각 자릿값이 더해진 값이 들어감.
    result = i + sum(a)

    if result == n:
        print(i)
        break

    if i == n:
        print(0)
