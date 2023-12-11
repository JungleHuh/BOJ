n = int(input())
user = []

for i in range(n):
    a,b = map(int, input().split())
    user.append([int(a),b])

for i in sorted(user, key = lambda x: x[0]):
    print(i[0], i[1])
