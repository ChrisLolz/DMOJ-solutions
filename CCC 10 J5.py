from collections import deque

moves = [[1,2],[2,1],[2,-1],[1,-2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

x,y = map(int,input().split())
start = [x,y]

x,y =map(int,input().split())
end = [x,y]

def possible(pos,move): #check if move is illegal
    if pos[0] + move[0] <= 8:
        if pos[0] + move[0] >= 1:
            if pos[1] + move[1] <= 8:
                if pos[1] + move[1] >= 1:
                    return True
                
def bfs(pos,end):
    if pos == end:
        print(0)
        return
    visited = [[False]*9 for _ in range(9)]
    steps = [[-1]*9 for _ in range(9)]
    steps[pos[0]][pos[1]] = 0
    queue = deque()
    queue.append(pos)
    visited[pos[0]][pos[1]] = True
    while queue:
        point = queue.popleft()
        
        for move in moves:
            if possible(point, move):
                newpoint = [point[0]+move[0],point[1]+move[1]]
                if not visited[newpoint[0]][newpoint[1]]:
                    queue.append(newpoint)
                    visited[newpoint[0]][newpoint[1]] = True
                    num_steps = steps[point[0]][point[1]]
                    steps[newpoint[0]][newpoint[1]] = num_steps+1
                    if newpoint == end:
                        print(num_steps+1)
                        return  

bfs(start,end)
