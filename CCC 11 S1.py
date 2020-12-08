N = int(input())
TC, SC = 0,0
for i in range(N):
    sentence = input()
    TC = TC + sentence.count("t")
    TC = TC + sentence.count("T")
    SC = SC + sentence.count("s")
    SC = SC + sentence.count("S")
    
if TC > SC:
    print("English")
elif TC < SC:
    print("French")
else:
    print("French")
