ang1 = int(input())
ang2 = int(input())
ang3 = int(input())
true = False
if ang1 == ang2:
    true = True
elif ang2 == ang3:
    true = True
elif ang1 == ang3:
    true = True

if (ang1 == 60 and ang2 == 60 and ang3 == 60):
    print("Equilateral")
elif (ang1+ang2+ang3 == 180 and true == True):
    print("Isosceles")
elif (ang1+ang2+ang3 == 180 and true == False):
    print("Scalene")
else:
    print("Error")
