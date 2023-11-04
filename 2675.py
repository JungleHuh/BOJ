Case = int(input())

for i in range(Case):
    N, S = input().split()
    for j in S:
        print(j*int(N), end ='')
    print()