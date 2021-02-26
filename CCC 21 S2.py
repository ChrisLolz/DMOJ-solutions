import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
K = int(input())

rows = [0]*M
cols = [0]*N
for i in range(K):
    temp = input().split()
    if temp[0] == "R":
        rows[int(temp[1])-1] += 1
    else:
        cols[int(temp[1])-1] +=1
count=0
for i in rows:
    for j in cols:
        if (i+j)%2 !=0:
            count+=1

print(count)
