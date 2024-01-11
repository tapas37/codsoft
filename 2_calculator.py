operator=input("enter an operator (+ - * / %): " )
num1=float(input("enter the firt number: "))
num2=float(input("enter the second number: "))

if operator =='+':
    result=num1+num2
    print(round(result,3))
elif operator =='-':
    result=num1-num2
    print(round(result, 3))
elif operator =='*':
    result=num1*num2
    print(round(result, 3))
elif operator =='/':
    result=num1/num2
    print(round(result, 3))
elif operator =='%':
    result=num1% num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")