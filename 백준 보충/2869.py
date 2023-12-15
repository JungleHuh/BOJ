import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

# 여기서 수학적인 공식으로 정리할 수 있었는데, 규칙을 찾아서 점화식만 세운 것이 아쉬움.
x = (c-b)//(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x)+ 1)