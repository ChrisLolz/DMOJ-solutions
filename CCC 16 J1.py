score = 0
for i in range(6):
    if input() == "W":
        score = score + 1
        
if score == 0:
    print("-1")

if score > 0:
    if score == 1 or score == 2:
        print(3)
    elif score == 3 or score == 4:
        print(2)
    elif score == 5 or score == 6:
        print(1)
