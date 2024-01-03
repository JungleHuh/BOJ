#컴퓨터의 특성, 반복문으로 해결. 반복문으로 문제를 어떻게 해결할 수 있을지를 생각하자
# 이 문제에서 나는 지극히 인간적인 생각 -> 3개를 한꺼번에 어떻게 비교할 수 있을까를 생각했다.
#그러나 이는 반복문으로 해결하기 어렵고, 하나하나씩 비교해주면서 가야한다. 
import sys
input = sys.stdin.readline

n = int(input())
word = list(input())
length = len(word)

for _ in range(n-1):
    other = list(input())
    for j in range(length):
        if word[j] != other[j]:
            word[j] = '?'

print(''.join(word))
