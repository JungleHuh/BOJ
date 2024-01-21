li = []

for i in range(3):
    k = list(map(int, input().split()))
    li.append(k)

for yoots in li:
    count_0 = yoots.count(0)  # 0의 개수 계산
    count_1 = yoots.count(1)  # 1의 개수 계산

    if count_0 == 1:
        print('A')
    elif count_0 == 2:
        print('B')
    elif count_0 == 3:
        print('C')
    elif count_0 == 4:
        print('D')
    elif count_1 == 4:
        print('E')
