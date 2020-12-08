word = input()
    
smile = word.count(":-)")
sad = word.count(":-(")

if smile == 0 and sad == 0:
    print("none")
elif smile == sad:
    print("unsure")
elif smile>sad:
    print("happy")
elif sad>smile:
    print("sad")
