import sys
input = sys.stdin.readline
line1 = list(map(int, input().split()))
N = line1[0]
M = line1[1]
lights = list(map(int,input().split()))
toggle = list(map(int,input().split()))

time = 0
count = lights.count(1)
while True:
    if count == 0:
        break
    if count <= time:
        break
    time = time+1

    if time<=M:
        switch = toggle[time-1]

        if lights[switch-1] == 1:
            lights[switch-1] = 0
            count = count - 1
        else:
            lights[switch-1] = 1
            count = count +1

print(time)
