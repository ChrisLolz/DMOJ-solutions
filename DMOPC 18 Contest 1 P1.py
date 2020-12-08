N = int(input())
A = input()
listA = list(map(int, A.split()))
listT = listA.copy()
listB = []
haszeros = False
solved = False
passed = True
firstOcc = 6969
lastOcc = 6969
middle = []

for i in range(len(listT)):
    if listT[i] == 0:
        haszeros = True
        if firstOcc == 6969:
            firstOcc = i
        lastOcc = i
    else:
        listB.append(listT[i])

if haszeros == True:
    if listB == sorted(listB):
        passed = True
    else:
        passed = False

if haszeros == False:
    if listA == sorted(listA):
        solved = True
    else:
        solved = False

if haszeros == True and lastOcc != 6969 and firstOcc !=6969 and passed == True:
    for i in range(firstOcc+1, lastOcc):
        if listT[i] != 0:
            middle.append(listT[i])
    middle = list(set(middle))
    if len(middle)>1:
        solved = False
    else:
        solved = True
if solved == True:
    print("YES")
else:
    print("NO")
