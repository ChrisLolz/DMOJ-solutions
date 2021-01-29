import math
N = int(input())
tides = list(map(int, input().split()))
tides.sort()

low = math.ceil(N/2)-1
hi = low+1

for i in range(N-1):
    if low-i >= 0:
        print(tides[low-i],end=" ")
    if hi+i < N:            
        print(tides[hi+i],end=" ")
        
print(tides[0])
