from collections import deque

N,K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque(0 for _ in range(2*N))

count = 0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = 0

    for i in range(N-2,-1,-1):
        if (robot[i] == 1) and (robot[i+1] == 0) and (belt[i+1] != 0):
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
        robot[N-1] = 0

    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1
    
    count += 1

    if belt.count(0) >= K:
        break
print(count)
    
