'''import sys
input = sys.stdin.readline

places = int(input())
people = list(map(int, input().split()))
a,b = map(int, input().split())
updated_people = []
count = 0

for i in range(places):
    k = (people[i] - a)
    updated_people.append(k)
    count += 1
    if k > 0:
        if k > b:
            m = k // b +1
            count += m
        else:
            count += 1
print(count)

'''

import sys
input = sys.stdin.readline

places = int(input())
people = list(map(int, input().split()))
a, b = map(int, input().split())
count = 0

for i in range(places):
    # 각 시험장의 응시생 수에서 총감독관이 감시할 수 있는 수를 뺌
    people[i] -= a
    count += 1

    # 응시생 수가 남아있으면 부감독관이 필요
    if people[i] > 0:
        # 부감독관이 감시할 수 있는 수로 나눈 몫을 더함
        count += (people[i] + b - 1) // b

print(count)




