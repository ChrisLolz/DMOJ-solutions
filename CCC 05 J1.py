day = int(input())
even = int(input())
end = int(input())

if day > 100:
    dayA = 0.25*(day-100)
else:
    dayA = 0
if day > 250:
    dayB = 0.45*(day-250)
else:
    dayB = 0

evenA = 0.15*even
evenB = 0.35*even
endA = 0.20*end
endB = 0.25*end

A = round(dayA+evenA+endA, 2)
B = round(dayB+evenB+endB,2)
if A>B:
    print("Plan A costs",A)
    print("Plan B costs",B)
    print("Plan B is cheapest.")
elif B>A:
    print("Plan A costs",A)
    print("Plan B costs",B)
    print("Plan A is cheapest.")
else:
    print("Plan A costs",A)
    print("Plan B costs",B)    
    print("Plan A and B are the same price.")
