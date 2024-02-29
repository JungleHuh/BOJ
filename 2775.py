T = int(input())
for _ in range(T):
    a = int(input())
    b = int(input())
    people = [j for j in range(1,b+1)]

    for x in range(a):
        for y in range(1,b):
            people[y] += people[y-1]
    print(people[-1])
