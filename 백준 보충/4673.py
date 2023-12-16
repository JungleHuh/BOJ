#str로 문자열로 만들고, map으로 int형으로 쪼개어 계산하는 것이 포인트
def d(n):
    n = n + sum(map(int, str(n)))
    #재귀인데 return 값 설정안해주는 실수
    return n

notSelfNum = set()

for i in range(1,10001):
    notSelfNum.add(d(i))

for j in range(1,10001):
    if j not in  notSelfNum:
        print(j)