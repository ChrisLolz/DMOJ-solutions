import sys
low = 1
high = 2*10**9
while low <= high:
    mid = int((low+high)/2)
    print(mid)
    sys.stdout.flush()
    string = input()
    if string == "SINKS":
        low = mid + 1
    elif string == "FLOATS":
        high = mid - 1
    else:
        break
