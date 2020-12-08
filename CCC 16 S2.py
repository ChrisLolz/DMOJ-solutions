ques = int(input())
N = int(input())
dmoj = list(map(int,input().split())) 
peg = list(map(int,input().split())) 
dmoj.sort()
total = 0
if ques == 1:
    peg.sort()
    for i in range(N):
        if dmoj[i]>peg[i]:
            total = total + dmoj[i]
        elif dmoj[i]<peg[i]:
            total = total + peg[i]
        else:
            total = total + dmoj[i]
elif ques == 2:
    peg.sort(reverse=True)
    for i in range(N):
        if dmoj[i]>peg[i]:
            total = total + dmoj[i]
        elif dmoj[i]<peg[i]:
            total = total + peg[i]
        else:
            total = total +dmoj[i]

print(total)
