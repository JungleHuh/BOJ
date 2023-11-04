import sys
input = sys.stdin.readline

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidates = [*map(int, input().split())]

#딕셔너리 만들어줌
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binary_Search(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end)//2
    
    if arr[mid] == target:
        return count.get(target)
    
    elif arr[mid] < target:
        return binary_Search(arr, target, mid+1, end)
    else:
        return binary_Search(arr, target, start, mid-1)
    
for target in candidates:
    print(binary_Search(cards, target, 0, len(cards)-1), end = " ")
