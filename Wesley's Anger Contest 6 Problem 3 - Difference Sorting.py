#DISCLAIMER: THIS DOES NOT WORK BECAUSE IT WILL TLE, MAYBE TRY CONVERTING THIS INTO JAVA OR C++ 

N = int(input())
K = 0
num = list(map(int, input().split()))
diff = 100000000000000
swap = -1

pos = N-1
while True:
    for j in range(N-1):
        if (num[pos] < num[j]) and (pos>j):
            if diff>(num[j] - num[pos]):
                diff = num[j] - num[pos]
                swap = j
    if swap != -1:
        num[pos], num[swap] = num[swap], num[pos]
        swap = -1
        pos = N-1
        if K < diff:
            K = diff
        diff = 10000000000000
    elif swap == -1:
        pos = pos-1
    if sorted(num) == num:
        break
print(K)
