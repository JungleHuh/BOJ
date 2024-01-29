mac = 0
for i in range(4):
    a,b = (map(int, input().split()))
    if i == 0:
        mac = mac + b
    else:
        mac = mac - a
        mac = max(mac, (mac + b))
print(mac)