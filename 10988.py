n = input()

for i in n:
    if i[::1] == i[::-1]:
        print(1)
    else:
        print(0)