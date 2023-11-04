#i(Exression)를 출력하는데, i의 범위는 1에서 시작해서 ~ 31전까지 Iterable......

n = [i for i in range(1, 31)]
    
for _ in range(28):
    num = int(input())
    n.remove(num)

print(min(n))
print(max(n))
