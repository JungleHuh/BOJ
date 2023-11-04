num_list = []
#리스트 만들어주기

for i in range(9):
    num_list.append(int(input()))

#배열에 요소를 넣는 것을 캐치하지 못함.

print(max(num_list))
print(num_list.index(max(num_list)) + 1)