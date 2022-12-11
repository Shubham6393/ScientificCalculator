import math
print("select the following operation")
print("1. Add")
print("2. subtract")
print("3. multiplication")
print("4. divide")
print("5. modules")
print("6. exponent")
print("7. square root")
print("8. sine ")
print("9. cose")
print("10. tangent")
print("11. radian to degree")
print("12. Degree to radian")
def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def mult(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
def mod(x,y):
    return (x%y)
def exp(x,y):
    return(math.pow(x,y))
def square_root(x):
    return (math.sqrt(x))
def sine(x):
    return (math.sin(x))
def cose(x):
    return(math.cos(x))
def tangent(x):
    return (math.tan(x))
def radian_degree(x):
    return(math.degrees(x))
def degree_radian(x):
    return (math.radians(x))

while True:
    choice=input("Enter the choice in number you want to perform(1/2/3/4/5/6/7/8/9/10/11/12)")
    if choice in ('1','2','3','4','5','6'):
        a=float(input("Enter the first number"))
        b=float(input("Enter the second number"))
        if choice=="1":
            print(a,"+",b,"=",add(a,b))
        elif choice=="2":
            print(a,"-",b,"=",sub(a,b))
        elif choice=="3":
            print(a,"*",b,"=",mult(a,b))
        elif choice=="4":
            print(a,"/",b,"=",div(a,b))
        elif choice=="5":
            print(a,"%",b,"=",mod(a,b))
        elif choice=="6":
            print(a,"exponent",b,"=",exp(a,b))
        next=input("Want to do more calculations??(yes/no)")
        if next=="no":
            break
    elif choice in ('7','8','9','10','11','12'):
        a=float(input("Enter the number"))
        if choice=="7":
            print("Square root of",a,"is",square_root(a))
        elif choice=="8":
            print("sine of",a,"is",sine(a))
        elif choice=="9":
            print("cose of",a,"is",cose(a))
        elif choice=="10":
            print("tangent of",a,"is",tangent(a))
        elif choice=="11":
            print("radian of",a,"to degree is",radian_degree(a))
        elif choice=="12":
            print("degree",a,"after converting into radian is",degree_radian(a))
        next = input("Want to do more calculations??(yes/no)")
        if next == "no":
            break
    else:
        print("Invalid choice, please choose the number given above.")