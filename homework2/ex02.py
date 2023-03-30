'''
Name: Pun VireakRoth
Class M3
'''
def multiply(num1, num2, num3):
    result = num1 * num2 * num3
    return result

# call multiply function
firstInput = int(input("a: "))
secondInput = int(input("b: "))
thirdInput = int(input("c: "))


print(f"{firstInput} * {secondInput} * {thirdInput} = {multiply(firstInput, secondInput, thirdInput)}");