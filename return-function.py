def powering(base,power):
    return pow(int(base),int(power))

base=input("Enter a number: ")
power=input("Enter the power to the number: ")

print("The power of "+str(power)+" to the base "+str(base)+" is "+str(powering(base,power)))