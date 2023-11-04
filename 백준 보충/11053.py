n = int(input())
lst = []
lst = list(map(int, input().split()))
count = 0

for i in range(n):
    if lst[i] < lst[i + 1]:
        count += 1
        continue
print(count)