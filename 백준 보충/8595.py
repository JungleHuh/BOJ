import sys
input = sys.stdin.readline

n = int(input())
hidden = input()
hidden_number = '1234567890'
tmp = ''

for i in hidden:
    if i in hidden_number :tmp += i
    else:tmp += ' '
k = list(map(int, tmp.split()))
print(sum(k))
    

'''
n = int(input())
s = input()
numbers = set("1234567890")  # 숫자를 검사할 때 set을 사용하면 빠르게 확인 가능합니다.
// c if c in numbers else ' ': 만약 문자 c가 numbers 집합에 속한다면 c를 선택하고, 그렇지 않으면 공백 ' '을 선택
// for c in s: 문자열 s의 각 문자 c에 대해 위의 표현식을 수행
tmps = ''.join([c if c in numbers else ' ' for c in s])  # 리스트 컴프리헨션과 join을 사용하여 효율적으로 문자열을 만듭니다.

print(sum(map(int, tmps.split())))

'''