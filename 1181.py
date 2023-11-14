import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
#집합으로 중복 제거
set_lst = set(lst)
lst = list(set_lst)
#사전순으로 정렬
lst.sort()
#문자열의 길이에 따라서 정렬
lst.sort(key = len)

for i in lst:
    print(i)