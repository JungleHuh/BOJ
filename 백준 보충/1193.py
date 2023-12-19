n = int(input())
i, num = 0, 0
while n > num:
    i += 1 #i는 line의 갯수
    num += i #num은 i번째 line에 속한 원소의 갯수

if i % 2 == 0:
    a = i - (num - n)
    b = (num -n) + 1
else:
    a = (num -n) + 1
    b = i - (num -n)

print(f'{a}/{b}')