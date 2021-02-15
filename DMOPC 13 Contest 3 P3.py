import sys
from collections import deque
input = sys.stdin.readline
N,H = input().split()
N,H = int(N),int(H)

field = []
for i in range(N):
    row = list(map(int,input().split()))
    field.append(row)
    
def dfs(field,end):
    visited = [[False]*end for _ in range(end)]
    stack = deque()
    stack.append([0,0])
    visited[0][0] = True
    while stack:
        current = stack.pop()
        if current[0]-1 >= 0:
            if 0<=abs(field[current[0]][current[1]]-field[current[0]-1][current[1]]) <= H:
                if not visited[current[0]-1][current[1]]:
                    visited[current[0]-1][current[1]] = True
                    stack.append([current[0]-1,current[1]])
        if current[1]-1 >= 0:
            if 0<=abs(field[current[0]][current[1]]-field[current[0]][current[1]-1]) <= H:
                if not visited[current[0]][current[1]-1]:
                    visited[current[0]][current[1]-1] = True
                    stack.append([current[0],current[1]-1])
        if current[0]+1 <= N-1:
            if abs(field[current[0]][current[1]]-field[current[0]+1][current[1]]) <=H:
                if not visited[current[0]+1][current[1]]:
                    visited[current[0]+1][current[1]] = True
                    stack.append([current[0]+1,current[1]])
        if current[1]+1 <= N-1:
            if 0<=abs(field[current[0]][current[1]]-field[current[0]][current[1]+1]) <=H:
                if not visited[current[0]][current[1]+1]:
                    visited[current[0]][current[1]+1] = True
                    stack.append([current[0],current[1]+1])
        if visited[N-1][N-1] == True:
            return True

if dfs(field,N):
    print("yes")
else:
    print('no')
