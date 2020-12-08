K = int(input())
boss = []
total = 0
for i in range(K):
    number = int(input())
    if number == 0:
        del boss[-1]
    else:
        boss.append(number)

for i in range(len(boss)):
    total = total + boss[i]

print(total)
