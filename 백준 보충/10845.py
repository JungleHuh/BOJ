import sys
input = sys.stdin.readline

n = int(input())
#처음에는 for문을 돌면서 list에 append해주려고 했음.
#그러나 애초에 for문으로 받은 값을 list에 넣어주는게 편할 것 같아서 바꿈.
cmds = [input() for _ in range(n)]

queue = []

for cmd in cmds:
	# 'push는 인자를 2개 받으니, split()을 사용해서 인자 2개를 구분해줌
    if 'push' in cmd.split()[0]:
    	#'push 1'을 'push' 와 '1'로 나누고,
        #'1'의 index가 1이니, cmd.split[1]을 append
        queue.append(cmd.split()[1])
    # 'push'와 다르게, 'pop'는 인자를 1개 받으니 split()으로 안받아도 됨.
    elif 'pop' in cmd:
    	#queue가 비어있지 않으면 pop하고
        print(queue.pop(0)) if queue else print(-1)
    elif 'size' in cmd:
        print(len(queue))
    elif 'empty' in cmd:
        print(0) if queue else print(1)
    elif 'back' in cmd:
        print(queue[-1]) if queue else print(-1)
    elif 'front' in cmd:
        print(queue[0]) if queue else print(-1)