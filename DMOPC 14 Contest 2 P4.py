import sys
N = int(sys.stdin.readline())
trees = []
psa = [0]
for i in range(N):
    trees.append(int(sys.stdin.readline()))

Q = int(sys.stdin.readline())

for i in range(1,N):
    if psa[0] == 0:
        psa[0] = trees[0]
    psa.append(psa[i-1] + trees[i])
while Q>0:
    query = list(map(int, sys.stdin.readline().split()))
    a = query[0]
    b = query[1]
    if a == 0:
        answer = psa[b]
    else:
        answer = psa[b]- psa[a-1]
    print(answer)
    Q = Q-1
