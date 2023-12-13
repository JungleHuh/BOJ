from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    cmd = input().split()
    if(cmd[0] == 'push_front'):
        q.appendleft(int(cmd[1]))
    elif(cmd[0] == 'push_back'):
        q.append(int(cmd[1]))
    elif(cmd[0] == 'pop_front'):
        print(q.popleft()) if q else print(-1)
    elif(cmd[0] == 'pop_back'):
        print(q.pop()) if q else print(-1)
    elif(cmd[0] == 'size'):
        print(len(q)) if q else print(0)
    elif(cmd[0] == 'empty'):
        print(0) if q else print(1)
    elif(cmd[0] == 'front'):
        print(q[0]) if q else print(-1)
    elif(cmd[0] == 'back'):
        print(q[-1]) if q else print(-1)



'''
from collections import deque

que = deque([])
print(que) #==> deque([])

# 값 추가
que.append(1)
print(que) #==> deque([1])
que.append(3)
print(que) #==> deque([1, 3])

que.append(3)
print(que) #==> deque([1, 3, 3])

# 좌측에 값 추가
que.appendleft(9)
print(que) #==> deque([9, 1, 3, 3])

# 특정 값의 개수 반환
print(que.count(1)) #==> 1

# 큐 복사
que2 = que.copy()
print(que2) #==> deque([9, 1, 3, 3])

# 큐 초기화
que2.clear()
print(que2) #==> deque([])

# 큐 이어붙이기
que2 = deque([5,6])
que.extend(que2)
print(que) #==> deque([9, 1, 3, 3, 5, 6])

# 큐 좌측에 이어붙이기
que2 = deque([7,7,7])
que.extendleft(que2)
print(que) #==> deque([7, 7, 7, 9, 1, 3, 3, 5, 6])

# 큐 특정 위치에 값 삽입 (위치,값)
que.insert(3,100)
print(que) #==> deque([7, 7, 7, 100, 9, 1, 3, 3, 5, 6])

# 특정 값의 인덱스 반환
print(que.index(100)) #==> 3

# pop은 큐의 맨 뒤(우측) 값을 반환하고 큐에서 삭제
print('poped item : ',que.pop()) #==> poped item :  6
print(que) #==> deque([7, 7, 7, 100, 9, 1, 3, 3, 5])

# pop은 큐의 맨 앞(좌측) 값을 반환하고 큐에서 삭제
print('left poped item : ',que.popleft()) #==> left poped item :  7
print(que) #==> deque([7, 7, 100, 9, 1, 3, 3, 5])

# 지정된 값을 큐에서 삭제
que.remove(7)
print(que) #==> deque([7, 100, 9, 1, 3, 3, 5])

# 큐 내용 반전
que.reverse()
print(que) #==> deque([5, 3, 3, 1, 9, 100, 7])

# 맨 뒤의 값을 pop한 후 앞에 삽입
que.rotate()
print(que) #==> deque([7, 5, 3, 3, 1, 9, 100])

# 큐의 최대 길이 설정, 최대길이를 넘을시 앞의 값 삭제
que = deque([1,2,3],maxlen=3)
que.append(9)
print(que) #==> deque([2, 3, 9], maxlen=3)
'''