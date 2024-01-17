N,M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))
arr.sort()

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end)//2
        cur = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                count += 1
                cur = arr[i]

        if count >= M:
            global ans
            start = mid + 1
            ans = mid 
        else:
            end = mid - 1

start = 1
end = arr[-1] - arr[0]
ans = 0

binary_search(arr,start,end)
print(ans)
