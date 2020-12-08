N = int(input())
graphspec = input()
long = graphspec.count('v')+graphspec.count('^')
if long == 0:
    long = 1
graph = [['.'] * N for i in range(long)]

newgraph = graph.copy()
x = 0
y = graphspec.count('^')-1
for i in range(len(graphspec)):
    if graphspec[i] == 'v':
        y = y+1
        graph[y][x] = "\\"
        x = x+1
    elif graphspec[i] == '>':
        graph[y][x] = "_"
        x = x+1
    elif graphspec[i] == '^':
        graph[y][x] = "/"
        x = x+1
        y=y-1

for i in range((long-1),-1,-1):
    if '\\' not in newgraph[i] and '_' not in newgraph[i] and '/' not in newgraph[i]:
        del graph[i]

for N in graph:
    print ("".join(map(str,N)))
