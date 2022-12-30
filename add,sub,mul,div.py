num1=int(input("Enter a number : "))
num2=int(input("Enter another number : "))
symbol=input("Enter the arthemetic name for its operation : ")
if symbol=="add":
    print("SUM = "+str(num1+num2))
elif symbol=="sub":
    print("SUB = "+str(num1-num2)) 
elif symbol=="multi":
    print("MULTIPLICATION = "+str(num1*num2))
elif symbol=="div":
    print("DIVISION = "+str(num1/num2))           
else:
    print("unvalid choice")    