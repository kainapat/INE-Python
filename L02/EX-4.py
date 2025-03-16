print("""Please select operation
1. Add
2. Subtract
3. Multiply
4. Divide""")
operation = int(input("Select operation form 1, 2, 3, 4 : "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operation == 1 :
    calculate =num1+num2
    print(num1,'+',num2 ,'=',(calculate))
elif operation == 2 :
    calculate =num1-num2
    print(num1,'-',num2 ,'=',(calculate))
elif operation == 3 :
    calculate =num1*num2
    print(num1,'*',num2 ,'=',(calculate))
elif operation == 4 :
    calculate =num1/num2
    print(num1,'/',num2 ,'=',(calculate))
else:
    print("operation error")