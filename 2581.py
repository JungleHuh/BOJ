import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
number = [i for i in range(a,b+1)]
odd_number = []

for num in number:
    odd = 0

    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                odd += 1
        if odd == 0:
            odd_number.append(num)
if len(odd_number) == 0:
    print(-1)
else:
    print(sum(odd_number), odd_number[0], sep = "\n")
