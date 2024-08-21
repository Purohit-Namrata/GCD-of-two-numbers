def computeGCD(x,y):
    while(y):
        x,y=y,x%y 
    return x

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
if(a<0):
    abs(a)
if(b<0):
    abs(b)

print("GCD is ",computeGCD(a,b))




        
