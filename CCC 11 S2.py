N = int(input())
ans = []
q = []
count = 0
for i in range(N):
    ans.append(input())
for i in range(N):
    q.append(input())

for i in range(N):
    if ans[i] == q[i]:
        count = count +1

print(count)
