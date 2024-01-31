import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split() ))
sorted_li = sorted(list(set(li)))
dic_list = dict(zip(sorted_li, list(range(len(sorted_li)))))

for i in li:
    print(dic_list[i])