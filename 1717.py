import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    root_x = find_parent(x, parent)
    root_y = find_parent(y, parent)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

numbers = set()
parent = {}
rank = {}

M, N = map(int, input().split())

for i in range(N):
    a, b, c = map(int, input().split())
    if a == 0:
        numbers.add((b, c))
        if (b, c) not in parent:
            parent[(b, c)] = (b, c)
            rank[(b, c)] = 0
    elif a == 1:
        if (b, c) in numbers:
            root_b = find_parent(b, parent)
            root_c = find_parent(c, parent)
            if root_b == root_c:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
