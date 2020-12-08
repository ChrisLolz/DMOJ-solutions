N, M = int(input()), int(input())
adj, noun = [], []
for i in range(N):
    adj.append(input())
for i in range(M):
    noun.append(input())

for i in range(N):
    for j in range(M):
        print(adj[i], "as", noun[j])
