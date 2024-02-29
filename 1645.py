import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lengths = [int(input()) for _ in range(n)]
start = 1
end = max(lengths)

while start <= end:
    mid = (start + end) //2

    line = sum(length//mid for length in lengths)

    if line >= m:    
        start = mid +1
    else:
        end = mid + 1
print(end)










