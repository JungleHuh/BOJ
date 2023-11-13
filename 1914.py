N = int(input())

def hanoi(N, start, to, via):
    if N == 1:
        print(start, to)
        return
    else:
        hanoi(N - 1, start, via, to)
        print(start, to)
        hanoi(N - 1, via, to, start)

print(2**N - 1)
if N <= 20:  # N이 20 이하인 경우에만 출력
    hanoi(N, 1, 3, 2)
