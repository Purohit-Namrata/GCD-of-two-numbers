def computeGCD(x,y):
    while(y):
        x,y=y,x%y
        
    return x

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))


print("GCD is ",computeGCD(a,b))




        