li = []
color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
range_value = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

for i in range(2):
    k = input()
    li.append(color.index(k))
a = li[0] 
b = li[1]
c = int(str(a) + str(b))

m = input()
h = color.index(m)
q = range_value[h]

res =  q *c
print(res)


