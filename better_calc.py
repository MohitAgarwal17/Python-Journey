num1=float(input("Enter first Number: "))
op=input("Enter Operator: ")
num2=float(input("Enter second Number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator")