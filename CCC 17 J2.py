N,K = int(input()), int(input())
total = 0
for i in range(K):
    total = total + (N*(10**(i+1)))

print(total + N)
