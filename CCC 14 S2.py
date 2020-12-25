N = int(input())
line1 = input().split()
line2 = input().split()
good = False
done = False
for i in range(N):
    partnerA = line1[i]
    partnerB = line2[i]
    for j in range(N):
        if partnerA == line2[j]:
            if partnerB == line1[j]:
                good = True
            else:
                done = True
    if partnerA == partnerB:
        done = True
        

if done == True:
    print('bad')
else:
    print('good')
