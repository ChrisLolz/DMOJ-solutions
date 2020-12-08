N = int(input())
ant, dav = 100, 100

for i in range(N):
    round = input().split()
    round[0]=int(round[0])
    round[1]=int(round[1])
    if round[0]<round[1]:
        ant = ant - round[1]
    elif round[0]>round[1]:
        dav = dav - round[0]

print(ant)
print(dav)
