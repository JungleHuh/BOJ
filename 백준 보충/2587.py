a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
list = [a,b,c,d,e]


print((a+b+c+d+e)//5)

for i in range(5):
    for j in range(5):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]
print(list[2])