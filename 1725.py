import sys
input = sys.stdin.readline

# 막대 개수
bar_count = int(input())

# 막대 높이 리스트
bar_heights = []
for _ in range(bar_count):
  height = int(input())
  bar_heights.append(height)

# 스택
stack = []

# 최대 면적
max_area = 0

# 각 막대 순회
for i in range(bar_count):
  current_index = i

  # 스택에 값이 존재하면 큰 값을 만날 때까지 pop
  while stack and stack[-1][1] > bar_heights[i]:
    popped_index, popped_height = stack.pop()
    # 현재 인덱스와 해당 인덱스까지의 차이와 높이를 곱해서 최대 넓이를 탐색
    area = (i - popped_index) * popped_height
    max_area = max(max_area, area)

  # 현재 막대 정보 스택에 추가
  stack.append((current_index, bar_heights[i]))

# 전체가 동일한 높이일 경우를 추가적으로 고려
while stack:
  popped_index, popped_height = stack.pop()
  area = (bar_count - popped_index) * popped_height
  max_area = max(max_area, area)

# 최대 면적 출력
print(max_area)
