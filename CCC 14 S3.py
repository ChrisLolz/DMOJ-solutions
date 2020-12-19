import sys
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    top = [0]
    branch = [0]
    lake = []
    done = True
    need = 1
    for i in range(N):
        top.append(int(sys.stdin.readline()))
    
    while True:
        if top[len(top)-1] == need:
            lake.append(top[len(top)-1])
            top.pop()
            need +=1
        elif branch[len(branch)-1] == need:
            lake.append(branch[len(branch)-1])
            branch.pop()
            need +=1
        elif len(top)>1:
            branch.append(top[len(top)-1])
            top.pop()
        else:
            done = False
            break
        if need -1 == N:
            break
    if done == True:
        print("Y")
    else:
        print("N")
