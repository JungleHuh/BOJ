MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"

def move(N, start, to):
    print(MSG_FORMAT(N, start, to))

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

result = hanoi(N, 'A', 'B', 'C')

N = int(input())



