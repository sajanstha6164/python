print(2**3)
def powering(base,power):
    result=1
    for num in range(power):
        result=result*base
    return result

print(powering(2,4))
