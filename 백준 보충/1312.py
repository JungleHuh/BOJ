#런타임 에러가 뜸 -> 뜨는 이유: 파이썬은 문자열을 소수점 15자리까지만 표시.
#문자열로 하면 당연히 엄청 큰 수에 대해서는 값을 저장할 수 없음을 기억하자.
import sys
input = sys.stdin.readline

a,b,c = map(float, input().split())

k = a/b
str_k = str(k)
p = str_k.split('.')[1][int(c) - 1]

print(p)


#새로운 풀이: 수학
import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
#i = 0일 때는 소수점 아님. i = 1부터 소수점 나타냄.
for i in range(c+1):
    ans = a//b
    a = (a%b)*10
    print(ans)





