import sys
input = sys.stdin.readline

n = input().strip()  # 문자열 양쪽의 공백을 제거하여 n을 공백 없는 문자열로 만듭니다.
m = int(input())
lst = []

for i in range(m):
    lst.append(input().split())

for j in lst:
    if j[0] == 'P':
        n = ''.join(n + j[1])
    elif j[0] == 'L':
        


