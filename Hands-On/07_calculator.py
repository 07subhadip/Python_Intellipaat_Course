def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def fdiv(a,b):
    return a//b

num1 = int(input("Enter 1st num : "))
num2 = int(input("Enter 2nd num : "))
sign = input("""Enter a number from 1 to 4
Check Options available to Your ->
(1 -> +)
(2 -> -)
(3 -> *)
(4 -> //)
: """)

if sign == "1":
    print(num1,"+",num2,"=",add(num1,num2))
elif sign == "2":
    print(num1,"-",num2,"=",sub(num1,num2))
elif sign == "3":
    print(num1,"*",num2,"=",mul(num1,num2))
elif sign == "4":
    if num2 != 0:
        print(num1,"//",num2,"=",fdiv(num1,num2))
    else:
        print("Math Error...")
else:
    print("Invalid Operator")