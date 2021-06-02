import sys
input = sys.stdin.readline

line1 = list(map(int,input().split()))
M = line1[0]
N = line1[1]
K = line1[2]
notes  = []
para = 0

for i in range(M):
    beats = list(map(int, input().split()))
    notes.append(beats)

for i in range(M):
    for j in range(M):
        for p in range(N-1):
            if notes[i][p] < notes[j][p]:
                if notes[j][p]-notes[i][p] == K:
                    if notes[j][p+1]-notes[i][p+1] == K:
                        para = para+1
            elif notes[i][p] > notes[j][p]:
                if notes[i][p] - notes[j][p] == K:
                    if notes[i][p+1] - notes[j][p+1] == K:
                        para=para+1

print(int(para/2))
