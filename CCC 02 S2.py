from math import gcd
num1 = int(input())
num2 = int(input())
fraction = 0
mixed = 0
if num1 % num2 == 0:
    fraction = int(num1/num2)
    print(fraction)
    
elif num1 % num2 != 0:
    mixed = num1//num2
    d = gcd(num1,num2)
    num1 = int(num1/d)
    num2 = int(num2/d)
    num1 = num1 % num2
    if mixed != 0:
        print(mixed," ",num1,"/",num2, sep='')
    else:
        print(num1,"/",num2, sep='')
