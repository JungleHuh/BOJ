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

tmps = ''.join([c if c in numbers else ' ' for c in s])  # 리스트 컴프리헨션과 join을 사용하여 효율적으로 문자열을 만듭니다.

print(sum(map(int, tmps.split())))

'''