##TLE's in batch 7

from collections import deque
import sys
input = sys.stdin.readline
M = int(input())
N = int(input())
grid = []

for i in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

end = [M,N]

def bfs(end):
    visited = [[False]*(N+1) for _ in range(M+1)]
    queue = []
    queue.append([1,1])
    visited[1][1] = True
    
    while queue:
        point = queue.pop(0)
        find = grid[point[0]-1][point[1]-1]
        for i in range(Mx):
            for j in range(Nx):
                if (i+1)*(j+1) == find:
                    newpoint = [i+1,j+1]
                    if not visited[newpoint[0]][newpoint[1]]:
                        queue.append(newpoint)
                        visited[newpoint[0]][newpoint[1]] = True
                        if newpoint == end:
                            return True
if bfs(end):
    print('yes')
else:
    print('no')
