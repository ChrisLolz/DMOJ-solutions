N = int(input())
for i in range(N):
    thing = input()
    if "M" in thing and "C" in thing:
        print("NEGATIVE MARKS")
    elif "M" not in thing and "C" not in thing:
        print("PASS")
    else:
        print("FAIL")
