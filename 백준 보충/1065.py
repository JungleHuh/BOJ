def hansu(k):
    cnt = 0
    for num in range(1,k+1):
        if num < 100:
            cnt += 1
        else:
            num = str(num)
            if int(num[1]) - int(num[0]) == int(num[2])- int(num[1]):
                cnt += 1
    return cnt
print(hansu(int(input())))