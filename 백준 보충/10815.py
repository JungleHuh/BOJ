'''
import sys
input = sys.stdin.readline

n = int(input())
condition_card = list(map(int, input().split()))

m = int(input())
given_card = list(map(int, input().split()))

for i in given_card:
    for j in range(n):
        if condition_card[j] == i:
            print(1, end = '')
        else:
            print(0, end = '')
        break
        
'''

'''
for i in range(n):
    for j in given_card:
        if condition_card[i] == j:
            print(1, end = '')
            break
        else:
            print(0, end = '')
            break
'''

'''
import sys
input = sys.stdin.readline

n = int(input())
condition_card = list(map(int, input().split()))

m = int(input())
given_card = list(map(int, input().split()))

for i in given_card:
    found = False  # 각 주어진 카드에 대해 조건 카드에 일치하는지 여부를 나타내는 변수를 초기화합니다.
    for j in range(n):
        if condition_card[j] == i:
            print(1, end=' ')
            found = True  # 조건 카드와 일치하는 카드를 찾았음을 표시합니다.
            break  # 찾았으니 더 이상 루프를 돌 필요가 없습니다.
    if not found:
        print(0, end=' ')
'''\

import sys
input = sys.stdin.readline

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

n = int(input())
condition_card = list(map(int, input().split()))
condition_card.sort()  # 조건 카드 리스트를 정렬합니다.

m = int(input())
given_card = list(map(int, input().split()))

for i in given_card:
    if binary_search(condition_card, i):
        print(1, end=' ')
    else:
        print(0, end=' ')
