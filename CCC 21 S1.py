N = int(input())

heights = list(map(int,input().split()))
widths = list(map(int,input().split()))

area = 0
        
for i in range(N):
    area = area+(widths[i]*(heights[i]+heights[i+1])/2)

print(area)
